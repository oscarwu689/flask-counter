from flask import Flask, jsonify

app = Flask(__name__)

counter = 0

@app.route("/visit", methods=["POST"])
def visit():
    global counter
    counter += 1
    return jsonify({"visits": counter})


@app.route("/", methods = ["GET"])
def home():
    return "Flask 訪問人數正常運作中"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)