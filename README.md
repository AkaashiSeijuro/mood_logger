# Mood of the Queue

This internal tool allows team members to log the mood of the ticket queue and visualize the emotional trends throughout the day.

---

## Overview

- Users can log their mood along with an optional note.
- A bar chart provides a real-time summary of moods for the current day.
- All data is stored in a Google Sheet for easy access and sharing.

---

## Running the App Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/mood-queue.git
    cd mood-queue
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add the Google Service Account JSON file:
    - Save it as `google_service_account.json` in the project directory.
    - This file should not be committed to the repository.

4. Update `app.py`:
    - Replace the `sheet_id` variable with the correct Google Sheet ID.
    - Share the Google Sheet with the service account email to enable editing.

5. Launch the app:
    ```bash
    streamlit run app.py
    ```

6. Open [http://localhost:8501](http://localhost:8501) in a web browser to use the app.

---

## Google Sheet Link

- [View-only Google Sheet](https://docs.google.com/spreadsheets/d/14jxf9L3UrFXDG6H_IYRvpFp7RhqL6DOv5q658DmpVKs/edit?usp=sharing)

---

## Security Notice

The `google_service_account.json` file contains sensitive credentials and should not be shared or committed to version control.

---

## Additional Notes

This app is designed to be easily deployable to the Streamlit Community Cloud if desired.
