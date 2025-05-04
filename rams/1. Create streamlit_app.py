# streamlit_app.py

import streamlit as st
import requests

st.title("SHL Assessment Recommender")
job_query = st.text_input("Enter a job title or role:")

if st.button("Get Recommendations"):
    if job_query:
        with st.spinner("Fetching recommendations..."):
            response = requests.post(
                "https://your-fastapi-app-url.com/recommend",  # Change this!
                json={"query": job_query}
            )
            if response.status_code == 200:
                data = response.json()
                st.success("Top Assessments:")
                for i, item in enumerate(data.get("recommendations", []), 1):
                    st.markdown(f"{i}. **{item['title']}** - *{item['category']}*\n> {item['description']}")
            else:
                st.error("Failed to get recommendations. Check FastAPI backend.")
