import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from backend.model import get_response

load_dotenv()

FAISS_DB_PATH = "faiss_db"
if not os.path.exists(FAISS_DB_PATH) or not os.listdir(FAISS_DB_PATH):
    print("FAISS index not found. Creating a new one...")
    os.system("python backend/ingest_data.py")

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/query", methods=["POST"])
def query_assistant():
    data = request.json
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"error": "Query cannot be empty"}), 400

    try:
        response = str(get_response(user_query))  # Force response to string
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)