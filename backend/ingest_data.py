import os
from dotenv import load_dotenv
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import gdown
from langchain_community.vectorstores import FAISS

# Download the .env file from Google Drive
file_id = '12NwweO_ivW0LV91M1M-HKU29fi7-zm9y'
url = f'https://drive.google.com/uc?id={file_id}'
output = ".env"
gdown.download(url, output, quiet=False)

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
FAISS_DB_PATH = os.getenv("FAISS_DB_PATH", "faiss_db")  # Default to "faiss_db" if not set

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set")

# Define some documents
documents = [
    Document(page_content="Meeting notes: Discuss project X deliverables."),
    Document(page_content="Reminder: Submit report by Friday."),
    Document(page_content="Upcoming event: Tech conference next Wednesday."),
]

# Initialize the embeddings model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Split the documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# Create the FAISS vector store
vector_db = FAISS.from_documents(docs, embeddings)

# Save the FAISS index locally
vector_db.save_local(FAISS_DB_PATH)

print(f"Documents successfully indexed and saved at: {FAISS_DB_PATH}")