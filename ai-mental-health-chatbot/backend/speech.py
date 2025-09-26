import tempfile
from pydub import AudioSegment
import whisper

class SpeechToText:
    def __init__(self, model_name='small'):
        try:
            self.model = whisper.load_model(model_name)
        except Exception as e:
            print('Whisper model failed to load:', e)
            self.model = None

    def transcribe_file(self, incoming_file_path):
        audio = AudioSegment.from_file(incoming_file_path)
        audio = audio.set_frame_rate(16000).set_channels(1)
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp:
            audio.export(tmp.name, format='wav')
            result = self.model.transcribe(tmp.name)
            return result.get('text','')
