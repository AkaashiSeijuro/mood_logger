# Mood of the Queue

This is a simple internal tool to log the mood of a ticket queue and visualize the emotional trends throughout the day.

---

## Goal

- Log moods with optional notes
- Visualize mood trends with a bar chart
- Data stored in a Google Sheet for easy sharing

---

## How to Run Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/mood-queue.git
    cd mood-queue
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your Google Service Account JSON file:
    - Save it as `google_service_account.json` in the project directory
    - Do not commit this file to GitHub

4. Update `app.py`:
    - Ensure the `sheet_id` variable matches your Google Sheet ID
    - Share your Google Sheet with the service account email

5. Run the app:
    ```bash
    streamlit run app.py
    ```

6. Open [http://localhost:8501](http://localhost:8501) in your browser to interact with the app.

---

## Google Sheet Link

- [Google Sheet (view-only)](https://docs.google.com/spreadsheets/d/14jxf9L3UrFXDG6H_IYRvpFp7RhqL6DOv5q658DmpVKs/edit?usp=sharing)

---

## Loom Walkthrough

If required, record a short Loom video showing:
- Submitting moods
- Viewing the bar chart
- Brief overview of the code

---

## Important

- Keep `google_service_account.json` private as it contains sensitive keys.
- Use `.gitignore` to exclude it from version control.

---

## Notes

- The app can be deployed to Streamlit Community Cloud if needed.
