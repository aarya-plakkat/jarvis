from flask import Blueprint, request, jsonify
from services.rag_service import answer

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    query = data.get("message", "")
    if not query.strip():
        return jsonify({"error": "message is required"}), 400
    response = answer(query)
    return jsonify({"response": response})
