from flask import Flask, jsonify

app = Flask(__name__)

config = {
    "details": "🧠 Nicht AFK",
    "state": "24/7 Online",
    "large_image": "logo",
    "large_text": "Custom Presence"
}

@app.route("/config")
def get_config():
    return jsonify(config)

@app.route("/set/<details>/<state>")
def set_config(details, state):
    config["details"] = details
    config["state"] = state
    return "Updated"

app.run(host="0.0.0.0", port=3000)
