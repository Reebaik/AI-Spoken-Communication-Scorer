# rubric_data.py

RUBRIC = {
    "Content & Structure": {
        "total_weight": 40,
        "metrics": {
            "Salutation Level": {
                "weight": 5,
                "max_score": 5,
                "rules": [
                    {"scoring_criteria": "No Salutation", "keywords": [], "score": 0},
                    {"scoring_criteria": "Normal", "keywords": ["hi", "hello"], "score": 2},
                    {"scoring_criteria": "Good", "keywords": ["good morning", "good afternoon", "good evening", "good day", "hello everyone"], "score": 4},
                    {"scoring_criteria": "Excellent", "keywords": ["i am excited to introduce", "feeling great"], "score": 5}
                ]
            },
            "Keyword Presence": {
                "weight": 30,
                "max_score": 30, # Max raw score is 30 (20 + 10)
                "rules": [
                    {"scoring_criteria": "Must have", "keywords": ["name", "age", "school", "class", "family"], "score": 20},
                    {"scoring_criteria": "Good to have", "keywords": ["hobbies", "interest", "goal", "dream", "fun fact", "unique"], "score": 10}
                ]
            },
            "Flow": {
                "weight": 5,
                "max_score": 5,
                "rules": [
                    {"scoring_criteria": "Order followed", "keywords": ["salutation", "name", "age", "class", "school", "optional details", "closing"], "score": 5},
                    {"scoring_criteria": "Order not followed", "keywords": [], "score": 0}
                ]
            }
        }
    },
    "Speech Rate": {
        "total_weight": 10,
        "metrics": {
            "Speech Rate (WPM)": {
                "weight": 10,
                "max_score": 10,
                "rules": [
                    {"scoring_criteria": ">161 wpm", "keywords": [], "score": 2},
                    {"scoring_criteria": "141-160 wpm", "keywords": [], "score": 6},
                    {"scoring_criteria": "111-140 wpm", "keywords": [], "score": 10},
                    {"scoring_criteria": "81-110 wpm", "keywords": [], "score": 6},
                    {"scoring_criteria": "<80 wpm", "keywords": [], "score": 2}
                ]
            }
        }
    },
    "Language & Grammar": {
        "total_weight": 20,
        "metrics": {
            "Grammar Errors": {
                "weight": 10,
                "max_score": 10,
                "rules": [
                    {"scoring_criteria": "0-3 errors/100 words", "keywords": [], "score": 10},
                    {"scoring_criteria": "4-6 errors/100 words", "keywords": [], "score": 8},
                    {"scoring_criteria": "7-9 errors/100 words", "keywords": [], "score": 6},
                    {"scoring_criteria": "10-12 errors/100 words", "keywords": [], "score": 4},
                    {"scoring_criteria": ">13 errors/100 words", "keywords": [], "score": 2}
                ]
            },
            "Vocabulary Richness": {
                "weight": 10,
                "max_score": 10,
                "rules": [
                    {"scoring_criteria": "0.9-1.0", "keywords": [], "score": 10},
                    {"scoring_criteria": "0.7-0.89", "keywords": [], "score": 8},
                    {"scoring_criteria": "0.5-0.69", "keywords": [], "score": 6},
                    {"scoring_criteria": "0.3-0.49", "keywords": [], "score": 4},
                    {"scoring_criteria": "0.2-0.29", "keywords": [], "score": 2},
                    {"scoring_criteria": "<0.2", "keywords": [], "score": 0}
                ]
            }
        }
    },
    "Clarity": {
        "total_weight": 15,
        "metrics": {
            "Filler Word Rate": {
                "weight": 15,
                "max_score": 15,
                "rules": [
                    {"scoring_criteria": "0 to 3%", "keywords": [], "score": 15},
                    {"scoring_criteria": "4 to 6%", "keywords": [], "score": 12},
                    {"scoring_criteria": "7 to 9%", "keywords": [], "score": 9},
                    {"scoring_criteria": "10 to 12%", "keywords": [], "score": 6},
                    {"scoring_criteria": "13% and above", "keywords": [], "score": 3}
                ]
            }
        }
    },
    "Engagement": {
        "total_weight": 15,
        "metrics": {
            "Sentiment": {
                "weight": 15,
                "max_score": 15,
                "rules": [
                    {"scoring_criteria": ">=0.9", "keywords": [], "score": 15},
                    {"scoring_criteria": "0.7-0.89", "keywords": [], "score": 12},
                    {"scoring_criteria": "0.5-0.69", "keywords": [], "score": 9},
                    {"scoring_criteria": "0.3-0.49", "keywords": [], "score": 6},
                    {"scoring_criteria": "<0.3", "keywords": [], "score": 3}
                ]
            }
        }
    }
}