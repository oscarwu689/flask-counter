from flask import Flask, jsonify
from upstash_redis import Redis
from dotenv import load_dotenv
import os


load_dotenv()
print(f"[DEBUG] redis client type: {type(Redis)}")

UPSTASH_URL = os.environ.get("UPSTASH_URL")
UPSTASH_TOKEN = os.environ.get("UPSTASH_TOKEN")

if not UPSTASH_URL or not UPSTASH_TOKEN:
    raise RuntimeError("❌ 請設定 UPSTASH_URL 和 UPSTASH_TOKEN 環境變數")

redis = Redis(
    url=os.environ.get("UPSTASH_URL"),
    token=os.environ.get("UPSTASH_TOKEN")
)

app = Flask(__name__)

@app.route("/visit", methods=["POST"])
def visit():
    visits = redis.incr("visit_count")
    return jsonify({"visits": visits})

@app.route("/", methods=["GET"])
def home():
    result = redis.get("visit_count")


    return f"目前訪問次數：{result}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)
