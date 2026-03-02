from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app) # This allows your HTML file to talk to this Python script

@app.route('/api/stats')
def get_stats():
    # Simulating real-time business metrics
    stats = {
        "total_users": random.randint(1000, 5000),
        "matches_today": random.randint(50, 200),
        "avg_vibe_score": f"{random.randint(60, 99)}%",
        "trending_genre": random.choice(["Dark Academia", "Sci-Fi", "Classic Literature", "Poetry"])
    }
    return jsonify(stats)

if __name__ == '__main__':
    # We run this on port 5001 so it doesn't fight with Project 1
    app.run(debug=True, port=5001)