

This repository contains two fully implemented and tested features:

1. **Blog Title Suggestor** – Generates relevant blog titles using LLMs from provided content.
2. **Transcript Diarization** – Performs speaker diarization and transcription on uploaded audio files.

All deliverables have been successfully completed and validated.

## Repository Structure

```
darwix-assessment/
│
├── blogtitlesuggestor/
│   └── ... (Django views and utility code for title generation)
|   └── ... manage.py
|   └── ... requirements.txt
|   └── ... README.md
│
├── transcript\ diarization/
│   └── ... app.py
|   └── ... requirements.txt
|   └── ... README.md
│
└── README.md
```

## ✅ Features Delivered

- Blog Title Suggestion using LLM APIs.
- Audio Transcription with Speaker Diarization.
- Functional endpoints for both features.
- End-to-end tested and ready for deployment.

---

## 🛠 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/gpawank4/darwix-assessment.git
cd darwix-assessment
```

### 2. Create a virtual environment and activate it

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If running diarization in Google Colab, dependencies may vary slightly (refer to in-app comments).

### 4. Run the Django app

```bash
cd blogtitlesuggestor
python manage.py runserver
```

## 🚀 Endpoints

### 1. Blog Title Suggestion

**POST** `/suggest-titles/`

**Request Body:**
```json
{
  "content": "Your blog content here"
}
```

**Response:**
```json
{
  "titles": [
        "**\"The AI Revolution: Harnessing Power, Ensuring Responsibility\"**",
        "**\"Rethinking Humanity: The Future of Artificial Intelligence and Its Impact\"**",
        "**\"AI: Balancing Innovation with Ethics in a Rapidly Changing World\"**"
    ]
}
```

---

### 2. Audio Transcription with Diarization

Accessible via Streamlit or REST API depending on deployment.

**Usage:**

- Upload an audio file via the frontend or API.
- Optionally specify number of speakers.
- Get back JSON-formatted transcription with speaker labels.

**Output Example:**
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

---

## 📦 Deployment Options

- Local via Streamlit (`streamlit run app.py`)
- Django for title suggestions (`python manage.py runserver`)
- API testable via Postman or browser

---

## 👨‍💻 Author

Developed and maintained by G Pawan Kumar Reddy.
