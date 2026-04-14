# Resume Analyzer

## Overview

Resume Analyzer is a backend-driven application built with FastAPI that evaluates how well a candidate’s resume matches a job description.

The system goes beyond simple keyword matching by introducing:
- category-aware skill analysis
- weighted scoring based on job requirements
- explainable feedback generation
- actionable suggestions for improvement

This project demonstrates how structured backend systems can simulate intelligent resume screening workflows.

---

## Key Features

- Resume upload (PDF / DOCX)
- Text extraction and parsing
- Skill extraction with alias normalization
- Skill comparison (matched, missing, extra)
- Category-based grouping (DevOps, Cloud, Backend, etc.)
- Match score (baseline)
- Weighted match score (category-aware)
- Category-level match summary
- Suggestion engine (strengths, improvements, feedback)
- Clean report generation API
- Input validation and error handling

---

## Example Output (Clean Report)

```json
{
  "candidate_name": "John Doe",
  "match_level": "Low",
  "match_score": 22.22,
  "weighted_match_score": 45.83,
  "matched_skills": ["AWS", "Docker"],
  "missing_skills": ["Ansible", "CI/CD"],
  "summary": "This resume currently has a low match...",
  "top_improvements": "...",
  "category_feedback": "...",
  "analyzed_at": "2026-04-12T..."
}
```

---

## Tech Stack

### Backend
- Python
- FastAPI
- Pydantic (planned)
- Uvicorn

### Processing
- pdfminer.six
- python-docx
- regex (re)

### Architecture
- modular service-based design
- clean separation of concerns
- reusable core analysis pipeline

---

## Project Structure

The project follows a modular service-based architecture:

```
backend/
│
├── app/
│   ├── main.py
│   │
│   ├── services/
│   │   ├── analyzer.py
│   │   ├── text_extractor.py
│   │   ├── resume_parser.py
│   │   ├── skill_extractor.py
│   │   ├── matcher.py
│   │   ├── skill_categorizer.py
│   │   ├── suggester.py
│   │   ├── report_builder.py
│   │   └── upload_handler.py
│   │
│   ├── data/
│   │   ├── skills.json
│   │   └── skill_categories.json
│   │
│   └── uploads/
│
└── requirements.txt
```

---

## API Endpoints

### 1. Full Analysis (Debug)
POST /analyze_resume

### 2. Clean Response
POST /analyze_resume_clean

### 3. Report Endpoint (Recommended)
POST /analyze_resume_report

---

## Scoring Logic

### Match Score
Basic percentage of matched skills between resume and job description.

### Weighted Match Score
Category-based scoring using weights such as:
- DevOps
- Cloud
- Backend
- Tools

Only categories present in the job description influence the final score.

---

## Suggestion System

The system generates:
- Summary (low / moderate / strong match)
- Strengths (matched skills)
- Improvements (missing skills)
- Highlight advice
- Category feedback (biggest skill gap)

This makes the output more actionable and user-friendly.

---

## Error Handling

The API handles:
- invalid file types
- empty uploads
- short/invalid job descriptions
- unreadable PDFs
- unexpected server errors

Uses:
- 400 for user input errors
- 500 for system errors

---

## Why This Project

This project focuses on building a real backend system, not just a demo.

Key design goals:
- explainable logic instead of black-box AI
- deterministic and testable outputs
- modular architecture
- production-style API design

---

## Current Status

### Completed
- core analysis pipeline
- scoring and suggestions
- report builder
- input validation
- clean API endpoints

### In Progress
- UI improvements
- response models (Pydantic)
- testing (pytest)
- Docker setup
- CI/CD pipeline

---

## Future Improvements

- React frontend
- LLM-based suggestion enhancement
- database for storing analysis history
- deployment (cloud)
- Docker Compose setup

---

## Author

Divyesh Joshi
