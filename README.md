# Resume Analyzer

## Overview
Resume Analyzer is a backend system built with FastAPI that evaluates how well a candidate’s resume matches a job description.

Unlike basic keyword matchers, this system introduces:
- Category-aware skill analysis (DevOps, Cloud, Backend, etc.)
- Weighted scoring based on job requirements
- Explainable feedback generation
- Actionable suggestions for improving resume alignment

The goal of this project is to simulate a production-style backend system that combines structured data processing with intelligent evaluation logic.

---

## Key Highlights
- Designed a modular backend architecture using FastAPI
- Built a skill extraction system with alias normalization and regex matching
- Implemented category-based grouping of skills using JSON-driven mappings
- Developed a weighted scoring algorithm based on job requirements
- Created category-level gap detection to identify major skill deficiencies
- Generated human-readable suggestions (strengths, improvements, targeted feedback)
- Designed system to be extensible for future AI/LLM integration

---

## Engineering Decisions
- Explainability over black-box AI  
  Scoring logic is transparent and easy to understand

- Separation of concerns  
  Skill extraction, categorization, scoring, and suggestion logic are modular

- Category-based reasoning  
  Skills are grouped into meaningful domains instead of flat keyword matching

- Weighted scoring  
  Important categories (e.g., DevOps, Cloud) influence results more than less relevant ones

---

## Features
- Resume upload (PDF, DOCX)
- Text extraction and parsing
- Skill extraction with alias handling
- Skill comparison (matched, missing, extra)
- Category grouping for both resume and job description
- Match score (baseline)
- Weighted match score (category-aware)
- Category-level match summary
- Intelligent suggestion generation

---

## Example Output (Simplified)
- Match Score: 22%
- Weighted Match Score: 45%
- Category Feedback:
  "The biggest gap is in DevOps-related skills, especially Kubernetes, Terraform, and Jenkins."

---

## Why This Matters
This system provides more meaningful feedback than traditional resume scanners by explaining why a candidate is a good or poor fit, not just returning a score.

---

## Tech Stack
- Python
- FastAPI
- Pydantic
- Regex (re)
- pdfminer.six
- python-docx

---

## Future Improvements
- Docker + deployment
- CI/CD pipeline
- Database for storing results
- Frontend dashboard
- LLM-based suggestion improvements

---

## Author
Divyesh Joshi
