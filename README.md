# AI Meeting Assistant 🎙️

An AI-powered meeting assistant that automatically transcribes meeting audio and generates structured meeting minutes including summaries, key points, decisions, risks, and action items.

This project demonstrates how to combine **Whisper STT**, **Llama-3 (Groq)** and **LangChain** to build a real AI productivity tool.

---

# Features 🚀

* Audio transcription using Whisper (Groq)
* Meeting summarization
* Key point extraction
* Decision tracking
* Action item generation
* Risk detection
* Audio recording or upload via Gradio
* Transcript cleaning
* Modular architecture

---

# Architecture 🏗️

```bash
Audio Input
    ↓
Whisper STT (Groq)
    ↓
Transcript Cleaning
    ↓
LangChain Pipeline
    ↓
Llama-3 LLM
    ↓
Structured Meeting Minutes
```

---

# Tech Stack ⚙️

## AI / LLM

* Groq API
* Llama-3-70B
* Whisper Large v3

## Frameworks

* LangChain
* Gradio

## Python Libraries

* python-dotenv
* requests
* regex

---

# Project Structure 📁

```bash
ai-meeting-assistant/

├── main.py
├── README.md
├── requirements.txt
├── sample-meeting.wav

├── ui/
│   └── gradio_ui.py

├── src/
│   ├── core/
│   │   ├── assistant.py
│   │   ├── llm.py
│   │
│   ├── utils/
│   │   ├── whisper_utils.py
│   │   ├── main_utils.py
```

---

# Installation 🔧

## Clone repository

```bash
git clone https://github.com/jsuryanm/ai-meeting-assistant.git

cd ai-meeting-assistant
```

## Create virtual environment

```bash
uv init 
uv venv --python 3.12
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

## Install dependencies

```bash
uv add -r requirements.txt
```

---

# Environment Setup 🔑

Create `.env` file:

```bash
GROQ_API_KEY=your_api_key_here
```

Get API key:

```bash
https://console.groq.com/
```

---

# Running the Application ▶️

Run Gradio UI:

```bash
python ui/gradio_ui.py
```

Open browser:

```bash
http://localhost:7860
```

---

# Example Output 📊

```bash
SUMMARY:
Sprint planning meeting discussing backend completion.

KEY POINTS:
• Backend finished
• UI testing pending

DECISIONS:
• Release scheduled next month

ACTION ITEMS:

Task | Owner | Deadline
UI Testing | John | Friday

RISKS:
Possible integration delays
```

---

# Learning Goals 🎯

This project helped me learn:

* Speech-to-text pipelines
* Prompt engineering
* LangChain chains
* LLM structured extraction
* AI system design
* Gradio UI development
* API integration

---


# Known Limitations 

* No speaker identification yet
* Requires clear audio
* No meeting history storage
* No real-time processing

---

# License 📄

MIT License

---

# Author 👨‍💻

**Surya**

---

# Acknowledgements 🙏

* Groq
* LangChain
* Whisper research
* Gradio

---

# Support ⭐

If you found this useful:

```bash
Star the repository ⭐
```
