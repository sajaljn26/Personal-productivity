import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
import gdown

# Download the .env file from Google Drive
file_id = '12NwweO_ivW0LV91M1M-HKU29fi7-zm9y'
url = f'https://drive.google.com/uc?id={file_id}'
output = ".env"
gdown.download(url, output, quiet=False)

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
FAISS_DB_PATH = os.getenv("FAISS_DB_PATH", "faiss_db")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set")

# Initialize the embeddings model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load the FAISS index
try:
    vector_db = FAISS.load_local(FAISS_DB_PATH, embeddings, allow_dangerous_deserialization=True)
    print("FAISS index loaded successfully.")
except Exception as e:
    raise ValueError(f"Error loading FAISS index: {e}")

# Create a retriever
retriever = vector_db.as_retriever()

# Initialize the Groq LLM
llm = ChatGroq(
    model_name="Llama3-8b-8192",  # Use model_name instead of model
    groq_api_key=GROQ_API_KEY
)

# Create a RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever
)

# Define a function to get a response
def get_response(query):
    try:
        # Use `invoke` instead of `run`
        result = qa_chain.invoke(query)
        return result
    except Exception as e:
        return f"Error generating response: {e}"

# Example usage
query = "What are the meeting notes about?"
response = get_response(query)
print(response)