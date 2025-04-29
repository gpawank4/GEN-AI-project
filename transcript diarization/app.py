import streamlit as st
import whisper
import tempfile
import torch
import subprocess
import numpy as np
import json

from pyannote.audio import Audio
from pyannote.audio.pipelines.speaker_verification import PretrainedSpeakerEmbedding
from pyannote.core import Segment
from sklearn.cluster import AgglomerativeClustering
import datetime
import wave
import contextlib

# Install packages if running locally
# !pip install -q git+https://github.com/openai/whisper.git
# !pip install -q git+https://github.com/pyannote/pyannote-audio

# Title
st.title("Audio Transcriber with Speaker Diarization")

# Upload file
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a"])

# Select options
num_speakers = st.number_input("Number of Speakers", min_value=1, max_value=10, value=2)
language = st.selectbox("Language", ["any", "English"])
model_size = st.selectbox("Model Size", ["tiny", "base", "small", "medium", "large"])

# Process if file is uploaded
if uploaded_file is not None:
    with st.spinner('Processing...'):

        # Save uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        # Always convert to proper WAV first
        converted_wav = tmp_path.rsplit('.', 1)[0] + '_converted.wav'
        subprocess.call(['ffmpeg', '-y', '-i', tmp_path, '-ar', '16000', '-ac', '1', converted_wav],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT)

        path = converted_wav

        # Whisper model
        model_name = model_size
        if language == 'English' and model_size != 'large':
            model_name += ".en"

        model = whisper.load_model(model_size)
        result = model.transcribe(path)
        segments = result["segments"]

        # Duration
        with contextlib.closing(wave.open(path,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)

        # Speaker embedding model
        embedding_model = PretrainedSpeakerEmbedding(
            "speechbrain/spkrec-ecapa-voxceleb",
            device=torch.device("cuda" if torch.cuda.is_available() else "cpu")
        )

        audio = Audio()

        def segment_embedding(segment):
            start = segment["start"]
            end = min(duration, segment["end"])
            clip = Segment(start, end)
            waveform, sample_rate = audio.crop(path, clip)
            return embedding_model(waveform[None])

        embeddings = np.zeros(shape=(len(segments), 192))
        for i, segment in enumerate(segments):
            embeddings[i] = segment_embedding(segment)

        embeddings = np.nan_to_num(embeddings)

        # Clustering
        clustering = AgglomerativeClustering(num_speakers).fit(embeddings)
        labels = clustering.labels_

        for i in range(len(segments)):
            segments[i]["speaker"] = f"SPEAKER {labels[i] + 1}"

        def format_time(secs):
            return str(datetime.timedelta(seconds=round(secs)))

        # Create JSON output
        output = []
        for segment in segments:
            entry = {
                "speaker": segment["speaker"],
                "start": format_time(segment["start"]),
                "end": format_time(segment["end"]),
                "text": segment["text"].strip()
            }
            output.append(entry)

        # Display JSON
        st.subheader("Transcription with Speaker Labels:")
        st.json(output)

        # Option to download JSON
        st.download_button(
            label="Download JSON",
            data=json.dumps(output, indent=4),
            file_name='transcription.json',
            mime='application/json'
        )
