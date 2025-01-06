from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Battlesnake Server is Running!"

@app.route("/start", methods=["POST"])
def start():
    return {"color": "#888888"}

@app.route("/move", methods=["POST"])
def move():
    return {"move": "up"}

@app.route("/end", methods=["POST"])
def end():
    return {}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
