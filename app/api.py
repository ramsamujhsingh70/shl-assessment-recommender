from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# CORS for frontend access (e.g., Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origin(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base URL for SHL
SHL_BASE_URL = "https://www.shl.com/en/assessments/"

# Keyword-to-assessment mapping
SKILL_MAP = {
    "java": ["coding-assessments", "problem-solving"],
    "python": ["technical-assessments", "problem-solving"],
    "frontend": ["cognitive-ability", "verbal-reasoning"],
    "backend": ["coding-assessments", "numerical-reasoning"],
    "sql": ["numerical-reasoning"],
    "cloud": ["technical-assessments"],
    "aws": ["technical-assessments"],
    "data": ["numerical-reasoning", "inductive-reasoning"],
    "ml": ["technical-assessments", "inductive-reasoning"],
    "communication": ["verbal-reasoning", "situational-judgement"],
    "leadership": ["leadership-assessments", "personality-questionnaires"],
    "sales": ["sales-assessments", "situational-judgement"],
    "personality": ["personality-questionnaires"],
    "reasoning": ["inductive-reasoning", "deductive-reasoning"],
    "testing": ["problem-solving", "cognitive-ability"],
    "project": ["situational-judgement", "leadership-assessments"],
}

# Assessment metadata
ASSESSMENT_DETAILS = {
    "coding-assessments": {"title": "Coding Assessments", "type": "Technical"},
    "problem-solving": {"title": "Problem Solving", "type": "Cognitive"},
    "technical-assessments": {"title": "Technical Assessments", "type": "Technical"},
    "cognitive-ability": {"title": "Cognitive Ability", "type": "Cognitive"},
    "verbal-reasoning": {"title": "Verbal Reasoning", "type": "Cognitive"},
    "numerical-reasoning": {"title": "Numerical Reasoning", "type": "Cognitive"},
    "inductive-reasoning": {"title": "Inductive Reasoning", "type": "Cognitive"},
    "deductive-reasoning": {"title": "Deductive Reasoning", "type": "Cognitive"},
    "leadership-assessments": {"title": "Leadership Assessments", "type": "Behavioral"},
    "personality-questionnaires": {"title": "Personality Questionnaires", "type": "Personality"},
    "sales-assessments": {"title": "Sales Assessments", "type": "Behavioral"},
    "situational-judgement": {"title": "Situational Judgement", "type": "Behavioral"},
}

# Backup list in case query matches are too few
RELATED_ASSESSMENTS = list(ASSESSMENT_DETAILS.keys())

def generate_recommendation(slug: str) -> dict:
    """Generate a mock assessment entry based on slug."""
    info = ASSESSMENT_DETAILS[slug]
    return {
        "assessment_name": info["title"],
        "url": f"{SHL_BASE_URL}{slug}",
        "test_type": info["type"],
        "duration": f"{random.choice([30, 40, 45, 60])} mins",
        "remote_testing": random.choice(["Yes", "No"]),
        "adaptive_support": random.choice(["Yes", "No"]),
        "difficulty": random.choice(["Easy", "Medium", "Hard"]),
        "relevance_score": round(random.uniform(6.5, 10.0), 2),
        "user_rating": round(random.uniform(3.5, 5.0), 1)
    }

@app.get("/recommend")
def recommend(query: str = Query(..., min_length=3)):
    """Main endpoint to recommend assessments based on a job/skill query."""
    query = query.lower()
    selected_slugs = set()

    # Match known skills from the query
    for keyword, slugs in SKILL_MAP.items():
        if keyword in query:
            selected_slugs.update(slugs)

    # If not enough matches, pad with related assessments
    while len(selected_slugs) < 5:
        selected_slugs.add(random.choice(RELATED_ASSESSMENTS))

    # Limit to max 15 results
    selected_slugs = list(selected_slugs)[:15]

    # Build the response
    results = [generate_recommendation(slug) for slug in selected_slugs]
    return {"results": results}
