import streamlit as st
import requests
from datetime import date

API_URL = "http://localhost:8000"

st.title("🗓️ Daily Growth")
st.subheader("Add Today's Progress!")

activity = st.text_input("1. What I did today:")
learning = st.text_input("2. What I learned:")
struggle = st.text_input("3. What I struggled with:")
pride = st.text_input("4. One thing I’m proud of:")
improvement = st.text_input("5. What I’ll improve tomorrow:")

selected_date = st.date_input("Date", value=date.today())

if st.button("Save Progress!"):
    payload = {
        "date": str(selected_date),
        "activity": activity,
        "learning": learning,
        "struggle": struggle,
        "pride": pride,
        "improvement": improvement,
    }

    res = requests.post(f"{API_URL}/create", json=payload)

    if res.status_code == 201:
        st.success("Progress added successfully! 🎉")
        st.balloons()
    else:
        st.error("Error adding progress 😕")
        st.write(res.text)


