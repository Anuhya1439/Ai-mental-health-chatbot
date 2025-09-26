from transformers import pipeline
from .config import config

class EmotionDetector:
    def __init__(self, model_name=None):
        model_name = model_name or config.EMOTION_MODEL
        self.pipeline = pipeline('text-classification', model=model_name, return_all_scores=True)

    def detect(self, text):
        preds = self.pipeline(text)
        if isinstance(preds, list) and len(preds) > 0:
            scores = preds[0]
            scores = sorted(scores, key=lambda x: x['score'], reverse=True)
            top = scores[0]
            return {
                'top_label': top['label'],
                'top_score': float(top['score']),
                'all': scores
            }
        return {'top_label':'neutral','top_score':0.0,'all':[]}
