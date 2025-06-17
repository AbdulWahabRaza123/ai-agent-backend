from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from main import ask_question
from agent_faiss import ingest_documents
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
UPLOAD_FOLDER = "data"
ALLOWED_EXTENSIONS = {".txt", ".md"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return os.path.splitext(filename)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    session_id = data.get("session_id")
    question = data.get("question")

    if not session_id or not question:
        return jsonify({"error": "Missing session_id or question"}), 400

    try:
        result = ask_question(session_id, question)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/upload", methods=["POST"])
def upload_document():
    if "file" not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed. Only .txt or .md accepted."}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    try:
        ingest_documents(file_path)
        return jsonify({"message": f"File '{filename}' uploaded and indexed successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
