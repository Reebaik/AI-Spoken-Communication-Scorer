# scoring_engine.py

from typing import Dict, Any, Optional

# FIX: Correct Imports to match the functions in the new metrics.py
from metrics import (
    compute_filler_word_score,
    compute_keyword_presence_score,
    compute_flow_score,
    compute_salutation_score,
    compute_sentiment_score,
    compute_grammar_score,
    compute_vocabulary_score,
    compute_wpm_score,
)

def score_transcript(transcript: str, rubric: Dict[str, Any], duration_seconds: Optional[float] = None) -> Dict[str, Any]:
    
    # --- Initial Checks ---
    if not transcript or not transcript.strip() or len(transcript.strip().split()) == 0:
        return {"overall_score": 0, "total_words": 0, "criteria": []}

    transcript = transcript.strip()
    total_words = len(transcript.split())

    results = []
    overall_score = 0.0

    for crit_name, crit_data in rubric.items():
        crit_weight = crit_data["total_weight"]
        crit_score = 0.0
        metric_results = []

        for metric_name, metric_data in crit_data["metrics"].items():
            max_score = metric_data.get("max_score", 0.0)
            weight = metric_data.get("weight", 0.0)
            metric_rules = metric_data.get("rules", [])
            raw = 0.0

            # ✅ Dispatch Logic: Correctly calls the tiered scoring functions and passes the 'rules'
            metric_key = metric_name.lower()

            if metric_key == "filler word rate":
                raw = compute_filler_word_score(transcript, metric_rules)

            elif metric_key == "keyword presence":
                raw = compute_keyword_presence_score(transcript, metric_rules)

            elif metric_key == "flow":
                raw = compute_flow_score(transcript, metric_rules)

            elif metric_key == "salutation level":
                raw = compute_salutation_score(transcript, metric_rules)

            elif metric_key == "sentiment":
                raw = compute_sentiment_score(transcript, metric_rules)

            elif metric_key == "grammar errors":
                raw = compute_grammar_score(transcript, metric_rules)

            elif metric_key == "vocabulary richness":
                raw = compute_vocabulary_score(transcript, metric_rules)

            elif metric_key == "speech rate (wpm)":
                raw = compute_wpm_score(total_words, duration_seconds, metric_rules)

            # --- FINAL SCORING CALCULATION (Weighted Normalization) ---
            # normalized = (raw / max_score) * weight
            normalized = (raw / max_score) * weight if max_score > 0 else 0.0

            crit_score += normalized

            metric_results.append({
                "metric_name": metric_name.title(),
                "metric_weight": weight,
                "raw_score": round(raw, 3),
                "max_score": max_score,
                "normalized_score": round(normalized, 3)
            })

        overall_score += crit_score

        results.append({
            "criterion_name": crit_name.title(),
            "criterion_weight": crit_weight,
            "criterion_score": round(crit_score, 2),
            "metrics": metric_results
        })

    return {
        "overall_score": round(overall_score, 2),
        "total_words": total_words,
        "criteria": results
    }