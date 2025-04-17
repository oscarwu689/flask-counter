from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = int(os.environ.get("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port)

@app.route("/visit", methods=["POST"])
def visit():
    visits = r.incr("visit_count")
    return jsonify({"visits": visits})

@app.route("/visit", methods=["GET"])
def home():
    count = int(r.get("visit_count") or 0)
    return f"目前訪問次數：{count}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)
