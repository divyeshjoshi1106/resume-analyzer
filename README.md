# 📄 Resume Analyzer API

An AI-inspired backend system that analyzes resumes against job descriptions and provides actionable insights.

This project extracts structured data from resumes, compares it with job requirements, calculates match scores, and generates personalized suggestions to improve alignment.

---

## 🚀 Features

### ✅ Resume Parsing
- Extracts:
  - Name
  - Email
  - Phone number
  - Links (GitHub, LinkedIn, etc.)
- Supports PDF and DOCX files

### ✅ Skill Extraction
- Uses alias-based matching (e.g., JS → JavaScript, CI/CD → Continuous Integration)
- Handles variations using regex and normalization
- Avoids false positives with safe matching logic

### ✅ Job Description Analysis
- Extracts required skills from job descriptions
- Uses the same extraction pipeline for consistency

### ✅ Skill Matching
- Compares:
  - Matched skills
  - Missing skills
  - Extra skills

### ✅ Scoring System
- Basic Match Score (skill overlap)
- Weighted Match Score (category-based weighting)

### ✅ Smart Suggestions
- Summary, strengths, improvements
- Highlight advice
- Category-based feedback

---

## 🧠 How It Works

Resume Upload → Text Extraction → Skill Extraction → Job Parsing → Matching → Scoring → Suggestions

---

## 🧱 Tech Stack

- FastAPI
- Python
- Regex-based NLP
- JSON (skills, categories)

---

## ⚙️ How to Run

1. Clone repo:
git clone https://github.com/your-username/resume-analyzer.git

2. Setup:
python -m venv venv
source venv/bin/activate

3. Install:
pip install -r requirements.txt

4. Run:
uvicorn app.main:app --reload

5. Open:
http://127.0.0.1:8000/docs

---

## 📌 Future Improvements
- Frontend (React)
- NLP (spaCy / embeddings)
- LLM-based suggestions
- Docker + CI/CD
