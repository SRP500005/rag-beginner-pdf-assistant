import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_answer(question, retrieved_results):

    context_parts = []

    for result in retrieved_results:
        context_parts.append(result["chunk"])

    context = "\n\n".join(context_parts)

    prompt = f"""
You are a helpful PDF question-answering assistant.

Answer the user's question only using the context provided below.

If the answer is not available in the context, say:
"I could not find this information in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text