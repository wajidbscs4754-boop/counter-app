import os
from flask import Flask
import redis

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Default App")
REDIS_HOST = os.getenv("REDIS_HOST", "cache")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

r = redis.Redis(host=REDIS_HOST, port=6379, password=REDIS_PASSWORD)

@app.route("/")
def home():
    count = r.incr("visits")
    return f"{APP_NAME}: is page ko {count} baar dekha gaya tha!"

app.run(host="0.0.0.0", port=5000)