import os
from pathlib import Path
from flask import Flask, send_from_directory
from routes.chat_routes import chat_bp

def create_app():
    root_dir = Path(__file__).resolve().parents[1]
    frontend_dir = root_dir / "frontend"
    app = Flask(__name__, static_folder=str(frontend_dir), static_url_path="")
    app.register_blueprint(chat_bp, url_prefix="/api")

    @app.route("/")
    def index():
        return send_from_directory(frontend_dir, "index.html")

    @app.route("/<path:filename>")
    def static_files(filename):
        return send_from_directory(frontend_dir, filename)
    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
