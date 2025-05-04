from app.shl_catalog import search_catalog, load_catalog
from typing import List

test_queries = [
    {"query": "Python developer role", "expected": ["Python Programming Challenge", "Full Stack Developer Simulation"]},
    {"query": "Project manager position", "expected": ["Project Manager Evaluation"]},
]

catalog = load_catalog()

def precision_at_k(results: List[str], expected: List[str], k: int = 5):
    hits = sum(1 for r in results[:k] if r in expected)
    return hits / k

def evaluate():
    total = 0
    score = 0
    for test in test_queries:
        results = search_catalog(test["query"], catalog)
        recommended_names = [r["assessment_name"] for r in results]
        p = precision_at_k(recommended_names, test["expected"])
        print(f'Query: {test["query"]}, Precision@5: {p:.2f}')
        score += p
        total += 1
    print(f"\nAverage Precision@5: {score / total:.2f}")

if __name__ == "__main__":
    evaluate()

