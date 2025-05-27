# Mood of the Queue

This tool allows users to log the mood of a ticket queue and visualize emotional trends throughout the day. All data is stored in a Google Sheet for easy sharing and tracking.

---

## Overview

- Users can log a mood entry with an optional note.
- A bar chart provides a summary of mood entries for the current day.

---

## Running the App

1. Clone the repository and navigate to the project directory.

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure that a Google Service Account JSON file is available in the project directory.  
   - This file contains the necessary credentials to access the Google Sheet.  
   - It should not be committed to version control.

4. In the code, confirm that the correct Google Sheet ID is used and that the sheet is shared with the service account email to allow editing.

5. Start the application:
    ```bash
    streamlit run app.py
    ```

6. Open the application in a web browser at the provided local URL.

---

## Google Sheet

A shared Google Sheet is used as the data store for this tool:
- [View-only Google Sheet](https://docs.google.com/spreadsheets/d/14jxf9L3UrFXDG6H_IYRvpFp7RhqL6DOv5q658DmpVKs/edit?usp=sharing)

---
