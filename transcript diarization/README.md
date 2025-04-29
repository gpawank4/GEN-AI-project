# 🎙️ Streamlit Audio Transcriber with Speaker Diarization

This app lets you upload an audio file (mp3, wav, m4a), transcribe it using OpenAI's Whisper model, and label speakers using diarization.

## 📦 Installation

Make sure you have Python 3.8+ and `ffmpeg` installed.

### 1. Clone the repo or download the files
```bash
git clone https://github.com/gpawank4/darwix-assessment.git
cd darwix-assessment
cd transcript\ diarization/
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

If you face any `torch`/`ffmpeg` issues:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

Make sure `ffmpeg` is installed:
```bash
sudo apt install ffmpeg  # (Linux/Debian)
# or
brew install ffmpeg       # (Mac)
```

---

## 🚀 Running the App
```bash
streamlit run app.py
```

Then open the URL shown in terminal (typically http://localhost:8501)

---

## ✅ How It Works

1. **Upload** your `.mp3`, `.wav`, or `.m4a` audio file.
2. **Select** model size, number of speakers, and language.
3. **Wait** as the file gets transcribed and speakers identified.
4. **View** the output in JSON format.
5. **Download** the result.

---

## 🛠️ Customization

To change the default values:
- Number of speakers, language, model size can be edited directly in the Streamlit app before upload.

---

## 🧠 Tech Stack
- Streamlit
- OpenAI Whisper
- PyAnnote for speaker embeddings
- Agglomerative clustering (sklearn)

---

## 📄 Output Format (JSON)
```json
[
    {
        "speaker": "SPEAKER 1",
        "start": "0:00:00",
        "end": "0:00:03",
        "text": "What's your interest in it Mr. Wayne?"
    },
    {
        "speaker": "SPEAKER 2",
        "start": "0:00:03",
        "end": "0:00:07",
        "text": "I want to borrow it for uh spelunking."
    },
    {
        "speaker": "SPEAKER 1",
        "start": "0:00:07",
        "end": "0:00:09",
        "text": "Spelunking?"
    },
    {
        "speaker": "SPEAKER 2",
        "start": "0:00:09",
        "end": "0:00:11",
        "text": "Yeah you know cave diving."
    },
    {
        "speaker": "SPEAKER 1",
        "start": "0:00:11",
        "end": "0:00:15",
        "text": "You're expecting to run into much gunfire in these caves."
    }
]
```
