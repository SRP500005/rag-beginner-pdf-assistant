from src.pdf_loader import load_pdf
from src.text_splitter import split_text
from src.embeddings import create_embeddings
from src.retriever import retrieve_chunks
from src.generator import generate_answer


pdf_path = "data/documents/bjp_government_20_policies_rag_sample.pdf"


# Step 1: Load PDF
text = load_pdf(pdf_path)


# Step 2: Split PDF into chunks
chunks = split_text(
    text,
    chunk_size=1000,
    chunk_overlap=200
)


# Step 3: Create embeddings
embeddings = create_embeddings(chunks)


# Step 4: User question
question = input("\nAsk a question about the PDF: ")


# Step 5: Retrieve relevant chunks
results = retrieve_chunks(
    question,
    chunks,
    embeddings,
    top_k=3
)


# Step 6: Generate final answer
answer = generate_answer(
    question,
    results
)


print("\nAnswer:")
print(answer)