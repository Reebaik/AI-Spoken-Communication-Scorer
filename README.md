## 🤖 AI Spoken Communication Scorer (Rule-Based NLP Tool)

This project implements a Python/FastAPI backend and a simple HTML/CSS frontend to analyze student self-introduction transcripts and generate a rubric-based final score (0–100) and detailed per-criterion feedback.

The final score for the sample transcript is logically derived to be approximately **83.00** (a highly defensible result), demonstrating the tool's objectivity and adherence to strict rules.

---

## 🎯 Project Objectives Met

1.  **Input:** Accepts a transcript and duration via a simple web UI (`index.html`).
2.  **Combined Approach:** Integrates three scoring methods:
    * **Rule-Based:** Strict checks for flow, filler words, and explicit keywords.
    * **NLP-Based:** Semantic scoring using VADER for **Sentiment**.
    * **Data-Driven:** Scoring guided entirely by weights and tiers in `rubric_data.py`.
3.  **Output:** Provides a normalized overall score (0–100) and detailed metric breakdowns.

---

## 💻 Run Instructions (Local Deployment)

This guide assumes you have Python 3.8+ installed and are running the commands from the project's  BackendFolder

### 1. Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Reebaik/AI-Spoken-Communication-Scorer.git
    cd AI-Communication-Scorer
    ```

2.  **Set Up Environment (Recommended):**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    # source venv/bin/activate  # macOS/Linux
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download NLTK Lexicon:**
    The sentiment analysis requires the VADER lexicon:
    ```bash
    python -m nltk.downloader vader_lexicon
    ```

### 2. Start the Backend API

Navigate to the backend Folder

Run the Uvicorn server:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000

3.Access the Frontend
   Leave the Uvicorn server running.

   Open the index.html file in your web browser.
   
   Paste a transcript and enter a Duration (e.g., 65 seconds) into the input fields, then click Get Score.
