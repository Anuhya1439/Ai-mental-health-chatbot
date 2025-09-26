from transformers import pipeline
from .config import config

class ChatBot:
    def __init__(self, model_name=None):
        model_name = model_name or config.RESPONSE_MODEL
        self.generator = pipeline('text-generation', model=model_name, max_length=150)

    def generate_reply(self, user_text, context=None):
        prompt = self._build_prompt(user_text, context)
        out = self.generator(prompt, num_return_sequences=1)
        text = out[0]['generated_text']
        reply = text[len(prompt):].strip()
        if len(reply) == 0:
            return "I hear you. Tell me more — what's on your mind right now?"
        return reply

    def _build_prompt(self, user_text, context=None):
        parts = []
        if context:
            parts.extend([f"User: {m}" for m in context[-config.MAX_HISTORY:]])
        parts.append(f"User: {user_text}")
        parts.append("Assistant:")
        return "\n".join(parts)
