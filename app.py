import logging
import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

# Banco dentro do volume persistente do pod
DB_PATH = "/data/events.db"

def init_db():
    # Garante que o diretório /data existe (importante em alguns setups)
    os.makedirs("/data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            payload TEXT NOT NULL,
            received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()

def save_event(event):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO events (payload) VALUES (?)",
        [json.dumps(event)]
    )
    conn.commit()
    conn.close()

def load_events():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT payload FROM events ORDER BY id DESC;")
    rows = c.fetchall()
    conn.close()
    return [json.loads(row[0]) for row in rows]

def create_app():
    app = Flask(__name__)
    CORS(app)
    logging.basicConfig(level=logging.INFO)

    init_db()

    @app.route("/webhook", methods=["POST"])
    def webhook():
        data = request.json
        save_event(data)
        app.logger.info(f"Webhook recebido e salvo: {data}")
        return jsonify({"status": "ok"}), 200

    @app.route("/events", methods=["GET"])
    def get_events():
        return jsonify(load_events()), 200

    @app.route("/")
    def index():
        return "API online!", 200

    return app
