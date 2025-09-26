from flask import Flask, render_template, request, jsonify
from .chatbot import ChatBot
from .emotion import EmotionDetector
from .speech import SpeechToText
from .config import config
import os

app = Flask(__name__, template_folder='templates')

bot = ChatBot()
emotion = EmotionDetector()
stt = SpeechToText()

HISTORY = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/message', methods=['POST'])
def message():
    data = request.json or {}
    text = data.get('text','')
    if not text:
        return jsonify({'error':'no text provided'}),400

    emo = emotion.detect(text)
    reply = bot.generate_reply(text, context=HISTORY)
    HISTORY.append(text)
    if len(HISTORY) > config.MAX_HISTORY:
        HISTORY.pop(0)

    return jsonify({'reply':reply, 'emotion':emo})

@app.route('/api/voice', methods=['POST'])
def voice():
    f = request.files.get('file')
    if not f:
        return jsonify({'error':'no file'}),400
    tmp_path = os.path.join('/tmp', f.filename)
    f.save(tmp_path)

    text = stt.transcribe_file(tmp_path)
    emo = emotion.detect(text)
    reply = bot.generate_reply(text, context=HISTORY)

    HISTORY.append(text)
    if len(HISTORY) > config.MAX_HISTORY:
        HISTORY.pop(0)

    return jsonify({'text':text,'reply':reply,'emotion':emo})

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
