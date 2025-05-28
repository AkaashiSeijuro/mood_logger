# Import required libraries
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Path to the Service Account JSON file
json_file = "Your_Service_Account.json"

# Google Sheets API authentication
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file(json_file, scopes=scope)
client = gspread.authorize(creds)

# Google Sheet configuration
sheet_id = "14jxf9L3UrFXDG6H_IYRvpFp7RhqL6DOv5q658DmpVKs"
sheet = client.open_by_key(sheet_id).sheet1

# Streamlit user interface
st.title("Mood of the Queue")

# Mood input selection
mood = st.selectbox(
    "Select your mood:",
    ["Angry", "Crying", "Happy", "Annoyed", "Irritated", "Just Alright", "Bored", "Confused", "In Love"]
)
note = st.text_input("Optional note:")

# Handle submission of mood entry
if st.button("Submit"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, mood, note])
    st.success("Mood logged successfully!")

# Visualize mood data for the current day
st.header("Today's Mood Summary")
data = pd.DataFrame(sheet.get_all_records())

if not data.empty:
    data["Timestamp"] = pd.to_datetime(data["Timestamp"])
    data["Date"] = data["Timestamp"].dt.strftime("%Y-%m-%d")
    today = datetime.now().strftime("%Y-%m-%d")
    today_data = data[data["Date"] == today]

    if not today_data.empty:
        mood_counts = today_data["Mood"].value_counts()
        fig, ax = plt.subplots()
        mood_counts.plot(kind="bar", ax=ax)
        ax.set_ylabel("Count")
        ax.set_xlabel("Mood")
        ax.set_title("Mood Counts for Today")
        st.pyplot(fig)
    else:
        st.write("No moods logged today.")
else:
    st.write("No data available.")
