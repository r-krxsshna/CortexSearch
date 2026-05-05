import ollama
from utils.logger import get_logger

logger = get_logger(__name__)

class LLMClient():

    MODEL_NAME = "mistral:latest"

    @staticmethod
    def generate(prompt: str) -> str:

        logger.info("Calling Ollama LLM...")

        response = ollama.chat(
            model=LLMClient.MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt},
            ]
        )

        return response["message"]["content"]