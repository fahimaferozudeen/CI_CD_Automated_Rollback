from flask import Flask, jsonify
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "v1")
STATUS = os.getenv("APP_STATUS", "healthy")


@app.route("/")
def home():
    return jsonify({
        "application": "Rollback Demo App",
        "version": VERSION,
        "status": STATUS
    })


@app.route("/health")
def health():
    if STATUS == "healthy":
        return jsonify({
            "status": "healthy",
            "version": VERSION
        }), 200

    return jsonify({
        "status": "unhealthy",
        "version": VERSION
    }), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)