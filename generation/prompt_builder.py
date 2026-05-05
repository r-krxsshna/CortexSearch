from typing import List

class PromptBuilder:

    @staticmethod
    def build_prompt(query:str, contexts: List[str]) -> str:

         context_text = "\n\n".join(contexts)

         prompt = f"""
You are an intelligent enterprise assistant.

Answer the question ONLY using the provided context.
If the answer is not in the context, say "I don't know."

Context:
{context_text}
         
Question:
{query}
         
Answer:
"""

         return prompt.strip()