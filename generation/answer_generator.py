from retrieval.hybrid_search import HybridSearch
from ranking.reranker import Reranker
from generation.prompt_builder import PromptBuilder
from generation.llm_client import LLMClient
from utils.logger import get_logger

logger = get_logger(__name__)

class AnswerGenerator:

    def __init__(self):

        self.search_engine = HybridSearch()
        self.reranker = Reranker()

    def generate_answer(self, query: str):

        logger.info("Generating answer...")

        retrieved = self.search_engine.search(
            query,
            top_k=10
        )

        reranked = self.reranker.rerank(
            query,
            retrieved,
            top_k=5
        )

        contexts = [
            item["content"]
            for item in reranked
        ]

        prompt = PromptBuilder.build_prompt(
            query,
            contexts
        )

        answer = LLMClient.generate(prompt)

        return {
            "query": query,
            "answer": answer,
            "contexts": contexts,
        }