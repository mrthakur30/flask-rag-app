from flask import Flask, jsonify, request
from config import Config
from ingest.ingest_serivce import ingest_text
from query.generate_answer import generate_answer
from store import vector_store

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    @app.route("/health",methods=["GET"])
    def health():
         return jsonify({"status": "ok"})
    
    @app.route("/ingest", methods=["POST"] )
    def ingest():
       data = request.get_json()

       if not data or "text" not in data:
           return jsonify({"error": "Missing 'text' field"}), 400

       ingest_text(data["text"])

       return jsonify({
           "message": "Ingestion successful",
           "stored_vectors": len(vector_store.vectors)
       })

    @app.route("/query", methods=["POST"])
    def query():
        data = request.get_json()

        if not data or "question" not in data:
            return jsonify({"error": "Missing 'question' field"}), 400

        answer = generate_answer(data["question"])

        return jsonify({
            "question": data["question"],
            "answer": answer
        })
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    
