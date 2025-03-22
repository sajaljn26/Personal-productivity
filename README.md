# AI-Powered Productivity Assistant

An AI-powered productivity assistant that helps you manage tasks, answer questions, and retrieve information using natural language processing (NLP) and vector databases.

## Features

- **Natural Language Querying**: Ask questions in plain English.
- **Task Management**: Retrieve and manage task-related information.
- **FAISS Vector Database**: Efficiently stores and retrieves document embeddings.
- **Hugging Face Embeddings**: Uses pre-trained models for semantic search.
- **Flask Backend**: REST API for handling queries.
- **Interactive Frontend**: Simple web interface for querying the assistant.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Vector Database**: FAISS
- **Embeddings**: Hugging Face (`all-MiniLM-L6-v2`)
- **Language Model**: Groq (Llama3-8b-8192)

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git (optional)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/ai-productivity-assistant.git
cd ai-productivity-assistant