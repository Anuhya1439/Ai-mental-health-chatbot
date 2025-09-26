# AI Mental Health Chatbot


An empathetic conversational agent combining text & voice emotion detection with an NLP response engine. Built with Flask + Hugging Face transformers for quick experimentation. Designed for demo / resume use — swap in Rasa or other systems for production.


## Highlights
- Emotion detection from text and audio
- Transformer-based response generator (Hugging Face pipeline)
- Simple, responsive web UI (record voice or type)
- Docker-ready


## Quick start
1. Clone repo
2. Copy `.env.example` -> `.env` and edit
3. Build and run with Docker Compose: `docker compose up --build`
4. Open http://localhost:5000


## Local (no Docker)
1. Create virtualenv: `python -m venv venv && source venv/bin/activate`
2. `pip install -r requirements.txt`
3. `FLASK_APP=backend/app.py flask run --host 0.0.0.0`


## Notes
- For better emotion recognition models, configure `EMOTION_MODEL` in `.env` to a Hugging Face emotion model.
- For speech-to-text, the repo demonstrates using Whisper local (requires ffmpeg).


