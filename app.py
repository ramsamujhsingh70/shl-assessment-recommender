import streamlit as st
import requests
import pandas as pd

# Page configuration
st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        h1, h2 {
            color: #2C3E50;
        }

        .card {
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-bottom: 15px;
            transition: transform 0.3s ease-in-out;
            width: 280px;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .stDownloadButton {
            background-color: #3498db;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
        }

        .stDownloadButton:hover {
            background-color: #2980b9;
        }

        footer {
            background-color: #2C3E50;
            color: white;
            padding: 10px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title(" 📃 SHL Assessment Recommender 📃")
st.caption("Find the most relevant skills and assessments based on your job role")

# Input
query = st.text_input("💼 Enter job role or field", placeholder="e.g., Java Developer")

# Sidebar settings
with st.sidebar:
    st.title("⚙️ Settings")
    min_rating = st.slider("⭐ Minimum User Rating", 1.0, 5.0, 3.0, 0.5)
    num_results = st.slider("🔢 Number of recommendations", 5, 15, 10)
    selected_difficulty = st.selectbox("🧠 Select Difficulty Level", ["All", "Easy", "Medium", "Hard"])
    remote_only = st.checkbox("🌐 Remote Testing Only")
    adaptive_support_only = st.checkbox("🤖 Adaptive Support Only")
    sorting_criteria = st.selectbox(" 🖨 Sort by", ["Relevance Score", "User Rating"])
    st.markdown("---")
    st.markdown("Crafted by **Ram Samujh Singh**")

# API endpoint
API_URL = "http://127.0.0.1:8000/recommend"

# Helper functions
def fetch_recommendations(query):
    try:
        res = requests.get(API_URL, params={"query": query})
        res.raise_for_status()
        return res.json().get("results", [])
    except Exception as e:
        st.error(f"❌ Failed to connect to API: {e}")
        return []

def get_difficulty_text(difficulty):
    return {"Easy": "🟢 Easy", "Medium": "🟠 Medium", "Hard": "🔴 Hard"}.get(difficulty, difficulty)

def get_rating_color(rating):
    if rating >= 4.5: return "rating-high"
    if rating >= 3.5: return "rating-medium"
    return "rating-low"

# Display logic
if query:
    results = fetch_recommendations(query)

    if not results:
        st.warning("🚫 No matching assessments found.")
    else:
        # Apply filters
        if selected_difficulty != "All":
            results = [r for r in results if r["difficulty"] == selected_difficulty]
        if remote_only:
            results = [r for r in results if r["remote_testing"] == "Yes"]
        if adaptive_support_only:
            results = [r for r in results if r["adaptive_support"] == "Yes"]
        results = [r for r in results if r["user_rating"] >= min_rating]

        # Sort
        if sorting_criteria == "Relevance Score":
            results = sorted(results, key=lambda x: x["relevance_score"], reverse=True)
        else:
            results = sorted(results, key=lambda x: x["user_rating"], reverse=True)

        results = results[:num_results]

        # Display cards
        st.subheader("⭐ Top Recommendations")
        col_count = min(num_results, 3)
        cols = st.columns(col_count)

        for i, item in enumerate(results):
            with cols[i % col_count]:
                with st.container():
                    st.markdown(f"<div class='card'>", unsafe_allow_html=True)
                    st.markdown(f"### [{item['assessment_name']}]({item['url']})")
                    st.markdown(f"- **Type**: {item['test_type']}")
                    st.markdown(f"- **Duration**: {item['duration']}")
                    st.markdown(f"- **Remote Testing**: {item['remote_testing']}")
                    st.markdown(f"- **Adaptive Support**: {item['adaptive_support']}")
                    st.markdown(f"- **Difficulty**: {get_difficulty_text(item['difficulty'])}")
                    st.markdown(f"- **Relevance Score**: {item['relevance_score']} / 10")
                    st.markdown(f"- **User Rating**: {item['user_rating']} ⭐")
                    st.markdown(f"</div>", unsafe_allow_html=True)

        # CSV Download
        df = pd.DataFrame(results)
        st.markdown("---")
        st.subheader("📥 Download Recommendations")
        st.download_button(
            label="Download as CSV",
            data=df.to_csv(index=False),
            file_name="shl_recommendations.csv",
            mime="text/csv",
            use_container_width=True,
            key="main_download_btn"
        )

# Footer
st.markdown("<footer>Crafted with ❤️ by Ram Samujh Singh</footer>", unsafe_allow_html=True)
