# LitAmor-VibeAnalytics
# 📊 LitAmor VibeAnalytics Dashboard

A real-time Business Intelligence (BI) prototype built for **Lit Amor**. This dashboard monitors platform health, user engagement, and matching trends using a decoupled Full-Stack architecture.

## 🚀 Key Features
* **Real-Time Data Streaming:** Uses asynchronous polling to fetch live metrics every 3 seconds without page refreshes.
* **Dynamic UI:** Responsive grid layout built with CSS Flexbox/Grid for cross-device compatibility.
* **RESTful API:** A Python-based backend that serves simulated business data via JSON.

## 🛠️ Tech Stack
* **Backend:** Python 3, Flask, Flask-CORS (REST API)
* **Frontend:** HTML5, CSS3 (Modern UI), JavaScript (Fetch API / Async-Await)
* **DevOps:** Git, Virtual Environments (.venv)

## 📈 Why this matters for Lit Amor
To scale a matching platform, decision-makers need to see **User Growth**, **Avg Compatibility (Vibe Score)**, and **Content Trends** in real-time. This project demonstrates my ability to build the internal tools required to monitor a high-growth startup's performance.

## ⚙️ How to Run
1. Activate the environment: `.\.venv\Scripts\Activate.ps1`
2. Install dependencies: `pip install flask flask-cors`
3. Launch the API: `python app.py` (Runs on Port 5001)
4. Open `index.html` in any modern browser.