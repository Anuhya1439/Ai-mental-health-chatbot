import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    HOST = os.getenv('HOST','0.0.0.0')
    PORT = int(os.getenv('PORT','5000'))
    EMOTION_MODEL = os.getenv('EMOTION_MODEL','distilbert-base-uncased-finetuned-sst-2-english')
    RESPONSE_MODEL = os.getenv('RESPONSE_MODEL','gpt2')
    MAX_HISTORY = int(os.getenv('MAX_HISTORY',6))

config = Config()
