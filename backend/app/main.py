from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from services.text_extractor import extract_text
from services.resume_parser import parse_resume_text
from services.skill_extractor import extract_skills
from services.matcher import (
    compare_skills,
    calculate_match_score,
    calculate_weighted_match_score,
)
from services.suggester import generate_suggestions
from services.skill_categorizer import categorize_skills, build_category_match_summary
from services.analyzer import analyze_resume_core
from services.report_builder import build_analysis_report
from services.upload_handler import validate_and_save_upload


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
ALLOWED_TYPES = {
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}


@app.get("/health")
def health():
    print("health endpoint")
    return {"status": "ok"}


@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400, detail="Only PDF and DOCX files are allowed"
        )

    content = await file.read()

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    print(file_path)

    with open(file_path, "wb") as f:
        f.write(content)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "saved_to": f"uploads/{file.filename}",
    }


@app.post("/parse_resume")
async def parse_resume(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400, detail="Only PDF and DOCX files are allowed"
        )

    content = await file.read()

    file_path = os.path.join(UPLOAD_DIR, file.filename)
    print(file_path)

    with open(file_path, "wb") as f:
        f.write(content)

    extracted_text = extract_text(file_path)

    resume_details = parse_resume_text(extracted_text)

    return {
        "resume_details": resume_details,
    }


@app.post("/analyze_resume")
async def analyze_resume(
    file: UploadFile = File(...), job_description: str = Form(...)
):
    if not job_description or not job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")

    if len(job_description.strip()) < 40:
        raise HTTPException(
            status_code=400,
            detail="Job description is too short. Please provide more details.",
        )

    if not file.filename:
        raise HTTPException(status_code=400, detail="No file was uploaded.")

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400, detail="Only PDF and DOCX files are allowed"
        )

    content = await file.read()

    if not content:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    safe_filename = os.path.basename(file.filename)
    file_path = os.path.join(UPLOAD_DIR, safe_filename)

    print(file_path)

    with open(file_path, "wb") as f:
        f.write(content)

    extracted_text = extract_text(file_path)

    resume_details = parse_resume_text(extracted_text)

    job_skills = extract_skills(job_description)

    job_skills_groups = categorize_skills(job_skills)

    resume_skills = resume_details.get("skills", [])

    resume_skills_groups = categorize_skills(resume_skills)

    skill_comparison = compare_skills(resume_skills, job_skills)

    match_score = calculate_match_score(skill_comparison["matched_skills"], job_skills)

    category_match_summary = build_category_match_summary(
        job_skills_groups, resume_skills_groups
    )

    suggestions = generate_suggestions(
        skill_comparison,
        match_score,
        category_match_summary,
        job_skills_groups,
    )
    weighted_match_score = calculate_weighted_match_score(category_match_summary)

    return {
        "resume_details": resume_details,
        "job_skills": job_skills,
        "skill_comparison": skill_comparison,
        "match_score": match_score,
        "suggestions": suggestions,
        "job_skills_groups": job_skills_groups,
        "resume_skills_groups": resume_skills_groups,
        "category_match_summary": category_match_summary,
        "weighted_match_score": weighted_match_score,
    }


@app.post("/analyze_resume_clean")
async def analyze_resume_clean(
    file: UploadFile = File(...), job_description: str = Form(...)
):

    try:
        job_description, file_path = await validate_and_save_upload(
            file, job_description
        )
        analysis_result = analyze_resume_core(file_path, job_description)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred during analysis."
        )

    return {
        "name": analysis_result["resume_details"]["name"],
        "match_level": analysis_result["suggestions"]["match_level"],
        "match_score": analysis_result["match_score"],
        "weighted_match_score": analysis_result["weighted_match_score"],
        "matched_skills": analysis_result["skill_comparison"]["matched_skills"],
        "missing_skills": analysis_result["skill_comparison"]["missing_skills"],
        "suggestions": analysis_result["suggestions"],
        "analyzed_at": analysis_result["analyzed_at"],
    }


@app.post("/analyze_resume_report")
async def analyze_resume_report(
    file: UploadFile = File(...), job_description: str = Form(...)
):
    try:
        job_description, file_path = await validate_and_save_upload(
            file, job_description
        )
        analysis_result = analyze_resume_core(file_path, job_description)
        report = build_analysis_report(analysis_result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred during analysis."
        )

    return report
