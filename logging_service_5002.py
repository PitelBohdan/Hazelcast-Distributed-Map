
from flask import Flask, request, jsonify
import sys
import uuid

app = Flask(__name__)
storage = {}

@app.route("/log", methods=["POST"])
def log_message():
    data = request.get_data(as_text=True)
    msg_id = str(uuid.uuid4())
    storage[msg_id] = data
    print(f"[{PORT}] Logged: {msg_id} => {data}")
    return '', 200

@app.route("/log/<msg_id>", methods=["GET"])
def get_message(msg_id):
    return storage.get(msg_id, "Not Found"), 200

if __name__ == "__main__":
    PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5002
    app.run(port=PORT)
