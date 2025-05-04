import json
import os
from typing import List, Dict


def load_catalog():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, "..", "shl_assessment.json")
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"❌ Failed to load catalog: {e}")
        return []


# ✅ Search function (case-insensitive, checks name and type)
def search_catalog(query: str, catalog: List[Dict]) -> List[Dict]:
    query_words = query.lower().split()
    results = []

    for assessment in catalog:
        name = assessment.get("assessment_name", "").lower()
        test_type = assessment.get("test_type", "").lower()

        if any(q in name or q in test_type for q in query_words):
            results.append(assessment)

    return results


