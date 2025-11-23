# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

# Import the corrected RUBRIC data and the scoring engine
from rubric import RUBRIC 
from scoring_engine import score_transcript

# =========================
# FASTAPI + CORS SETUP
# =========================

app = FastAPI()

# FIX: Allows the frontend (running on a different port) to communicate with the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500", "*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# REQUEST MODEL
# =========================

class ScoreRequest(BaseModel):
    transcript: str
    duration_seconds: Optional[float] = None 

# =========================
# MAIN ENDPOINT
# =========================

@app.post("/score")
def auto_score(req: ScoreRequest):
    
    if not RUBRIC:
        return {"error": "Rubric data failed to load."}, 500

    result = score_transcript(
        transcript=req.transcript,
        rubric=RUBRIC,
        duration_seconds=req.duration_seconds
    )
    
    return result

# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)