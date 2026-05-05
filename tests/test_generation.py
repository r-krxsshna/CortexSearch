from generation.answer_generator import AnswerGenerator

generator = AnswerGenerator()

query = "How many sick leaves are allowed?"

response = generator.generate_answer(query)

print("ANSWER:\n", response["answer"])
print("\nSOURCES:\n")

for s in response["contexts"]:
    print("-", s[:100].replace("\n", " "), "...")