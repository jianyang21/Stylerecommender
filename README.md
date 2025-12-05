# Style Recommender App

This project is a fashion and product recommendation application built using React and a Retrieval-Augmented Generation (RAG) pipeline. The app suggests relevant products based on user inputs, preferences, or textual descriptions.

## Features

- Personalized product recommendations based on user queries.
- RAG-based intelligence for context-aware and accurate suggestions.
- Product search and filtering through natural language inputs.
- Responsive and clean user interface built using React.
- Scalable architecture for extending the product dataset and improving recommendations.

## How It Works

1. The user enters a query (e.g., "suggest formal shoes under 1500").
2. The backend retrieves relevant product vectors from a vector database.
3. An LLM processes the retrieved context and generates refined recommendations.
4. The frontend displays the final product suggestions.

## Tech Stack

### Frontend
- React
- JavaScript (or TypeScript)
- Axios or Fetch for API communication
- CSS, Tailwind, or custom styles

### Backend / AI
- RAG pipeline (Retriever + LLM Generator)
- Vector database (FAISS, Pinecone, Chroma, etc.)
- Embedding model for indexing products
- Node.js or Python backend for API endpoints

### Data Layer
- Product dataset stored in JSON or a database
- Vector index for similarity search

## Project Structure (Generic)

