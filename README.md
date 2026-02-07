# 🗓️ Daily Growth Tracker

Daily Growth Tracker is a simple personal progress logging app that helps users reflect on their day and build consistency over time.

The app allows users to record daily activities, learnings, struggles, and improvements using a clean web interface.

This project focuses on **basic full-stack Python development** using Streamlit and FastAPI.

---

## 🚀 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **Storage:** JSON (file-based)  
- **Language:** Python  

---

## 📂 Project Structure
dailygrowth/
│
├── api/
│ └── main.py # FastAPI backend
│
├── ui/
│ └── app.py # Streamlit frontend
│
├── data/
│ └── progress.json # Stored daily logs
│
└── requirements.txt

---

## ✨ Features

- 📝 Log daily progress with reflection prompts
- 📅 Store daily entries by date
- 🔌 FastAPI backend for data handling
- 🎨 Streamlit frontend for user interaction
- 🧠 Simple and beginner-friendly architecture

---

Link: https://daily-growth-tracker-6.streamlit.app/

## ▶️ Running the App Locally

```bash
1️⃣ Clone the repository
git clone https://github.com/your-username/daily-growth-tracker.git
cd daily-growth-tracker
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Start the FastAPI backend
uvicorn api.main:app --reload
The API will be available at:

http://localhost:8000
You can test it using:

http://localhost:8000/docs
4️⃣ Start the Streamlit frontend
Open a new terminal and run:

streamlit run ui/app.py
The app will open in your browser at:

http://localhost:8501
