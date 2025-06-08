
from flask import Flask, request, jsonify
import requests
import random
import os

app = Flask(__name__)

# Список бекендів (лог-сервісів)
logging_services = os.environ.get("LOGGING_SERVICES", "").split(",")

@app.route("/msg", methods=["POST"])
def send_msg():
    data = request.get_data(as_text=True)
    target = random.choice(logging_services).strip()
    requests.post(f"{target}/log", data=data)
    return '', 200

@app.route("/msg/<msg_id>", methods=["GET"])
def get_msg(msg_id):
    target = random.choice(logging_services).strip()
    response = requests.get(f"{target}/log/{msg_id}")
    return response.text, 200

if __name__ == "__main__":
    app.run(port=5000)
