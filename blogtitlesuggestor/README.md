# 🧠 Blog Title Generator using Groq + LangChain + Django

This Django app takes a blog post as input and uses the `llama3-70b-8192` model from **Groq** via **LangChain** to generate 3 human-like, creative blog title suggestions.

---

## 🔧 Requirements

- Python 3.9 or higher
- Virtual environment (recommended)
- Groq API key (get it from https://console.groq.com/keys)

---

## 📦 Installation

### 1. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Set Your Groq API Key

Open `blog/views.py` and set your Groq API key:

```python
groq_api_key = "your_groq_api_key_here"
```

Replace it with the API key you copied from https://console.groq.com/keys.

---

## 🚀 Run the Django Server

From the root of your project (where `manage.py` is located):

```bash
python manage.py runserver
```

This will start your server at:

```
http://127.0.0.1:8000/
```

---

## 📮 Make Requests via Postman

1. Open [Postman](https://www.postman.com/).
2. Create a new request:
   - Method: `POST`
   - URL: `http://127.0.0.1:8000/suggest-titles/`
   - Headers: 
     - `Content-Type`: `application/json`
   - Body → `raw` → `JSON`:

```json
{
    "content": "Artificial Intelligence (AI) has revolutionized the world dramatically over the past decade. Companies across various industries are harnessing AI to automate tasks, personalize services, and gain deep insights into consumer behavior. In healthcare, AI-driven diagnostics have led to faster and more accurate detection of diseases. In the financial sector, AI algorithms monitor transactions in real-time to detect fraudulent activities. The education sector is leveraging AI for personalized learning experiences and intelligent tutoring systems. Despite these advancements, AI raises ethical concerns around bias, privacy, and job displacement. Governments and organizations are working on establishing ethical guidelines to ensure AI is developed and used responsibly. Researchers are focusing on explainable AI to make algorithms transparent and understandable to humans. The future promises even deeper integration of AI into our daily lives, with smart cities, autonomous vehicles, and virtual assistants becoming increasingly common. Preparing the workforce for AI-driven changes through reskilling and continuous education will be crucial. Businesses must strike a balance between innovation and responsibility to fully realize AI's potential while safeguarding societal interests. Artificial Intelligence is not just a technological shift; it represents a fundamental rethinking of how humanity interacts with technology, information, and each other in the 21st century."
}
```

3. Click **Send**.

### ✅ You’ll get a response like:

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

## 🧾 File Structure

```
blogtitlesuggestor/
├── blog/
│   ├── views.py
│   ├── urls.py
├── blogtitlesuggestor/
│   ├── settings.py
│   ├── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🛠 Common Issues

### ❌ ModuleNotFoundError: No module named 'langchain_groq'

Run:

```bash
pip install langchain langchain_groq groq
```

Or just:

```bash
pip install -r requirements.txt
```

---

## ❤️ Credits

Built using:

- [LangChain](https://www.langchain.com/)
- [Groq](https://www.groq.com/)
- [Django](https://www.djangoproject.com/)

---

## 💡 Tip

You can enhance the title generation by modifying the prompt or using LangChain tools like memory, output parsers, or chaining with document loaders.

---
