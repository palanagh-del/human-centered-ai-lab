# RAG Learning Notes

## What is RAG?

RAG stands for Retrieval-Augmented Generation.

It means an AI system first retrieves relevant information from documents, then uses that information as context to generate an answer.

## Why RAG is useful

RAG is useful because large language models may not know the latest, private, or document-specific information. RAG helps make answers more grounded by connecting the model to external sources.

## Basic RAG pipeline

1. Load documents
2. Split documents into smaller chunks
3. Convert chunks into embeddings
4. Store embeddings in a vector database
5. Retrieve relevant chunks when the user asks a question
6. Give the retrieved context to the LLM
7. Generate an answer based on that context

## Important terms

### Chunking
Breaking a long document into smaller parts.

### Embeddings
Converting text into numbers so that similar meanings can be compared.

### Vector database
A database that stores embeddings and helps find similar pieces of text.

### Retriever
The part of the system that searches for relevant chunks.

### Context
The retrieved text given to the LLM before it answers.

## Why RAG matters for human-centered AI

RAG is not only a technical method. It also affects how users understand, trust, and evaluate AI answers.

Important research questions:

- Can users understand where the AI answer came from?
- Does showing sources improve trust?
- Can RAG reduce hallucination?
- Can users over-trust answers just because sources are shown?
- How should RAG-based financial advice show uncertainty?

## My next step

Build a tiny RAG demo using 2–3 simple documents, Python, Chroma, and Streamlit.
