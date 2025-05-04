# 📊 SHL Assessment Recommender

A GenAI-powered application that recommends SHL assessments based on job roles using semantic matching and filters.

---

## 🚀 Live Demo

- **Frontend (Streamlit)**: [Streamlit App](https://appapppy-5sra3zs3mktpvzbg9ca7cv.streamlit.app/)
- **Backend (FastAPI)**: [API Endpoint](https://shl-assessment-recommender-0btf.onrender.com)

---

## 🧠 How It Works

1. **User Input**: Enter a job title or skill (e.g., "Java Developer").
2. **Backend (FastAPI)**: Processes query using keyword mapping and returns relevant SHL assessments.
3. **Frontend (Streamlit)**: Displays recommendations as interactive cards with filters (rating, difficulty, remote, etc.).

---

## 🛠 Technologies Used

| Layer     | Tech Stack         |
|-----------|--------------------|
| Frontend  | Streamlit          |
| Backend   | FastAPI, Uvicorn   |
| Deployment| Streamlit Cloud, Render |
| Language  | Python 3.10+       |

---

## 📁 Project Structure

shl-assessment-recommender/
│
├── api.py # FastAPI backend with recommendation logic
├── requirements.txt # Dependencies for backend
├── frontend.py # Streamlit frontend (optional filename)
└── README.md # You're here!

yaml
Copy
Edit

---

## ⚙️ Backend Setup (Local)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI app
uvicorn api:app --reload
🌐 Deployment
Backend on Render
Create new web service.

Connect to your GitHub repo.

Set Start Command:

nginx
Copy
Edit
uvicorn api:app --host 0.0.0.0 --port 10000
Add requirements.txt

Done! Your API will be deployed.

Frontend on Streamlit Cloud
Upload your Streamlit app (e.g., frontend.py)

Ensure it uses the deployed API URL (https://...render.com/recommend)

Deploy!

🧪 Sample API Usage
http
Copy
Edit
GET /recommend?query=data scientist
Sample Response:
json
Copy
Edit
{
  "results": [
    {
      "assessment_name": "Numerical Reasoning",
      "url": "https://www.shl.com/en/assessments/numerical-reasoning",
      "test_type": "Cognitive",
      "duration": "45 mins",
      ...
    }
  ]
}
🙋‍♂️ Author
Built by Ram Samujh Singh
💼 Engineering Student | 💻 Passionate about AI + Web Dev

📄 License
MIT License — use freely and improve it!

yaml
Copy
Edit

---

Would you like me to fill in your actual **Streamlit app URL** in the README before you copy it?







