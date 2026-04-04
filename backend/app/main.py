from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import os
from services.text_extractor import extract_text
from services.resume_parser import parse_resume_text
from services.skill_extractor import extract_skills
from services.matcher import compare_skills, calculate_match_score
from services.suggester import generate_suggestions

app = FastAPI()

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

    parsed_data = parse_resume_text(extracted_text)

    return {
        "parsed_data": parsed_data,
    }


@app.post("/analyze_resume")
async def analyze_resume(
    file: UploadFile = File(...), job_description: str = Form(...)
):
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

    parsed_data = parse_resume_text(extracted_text)

    job_details = extract_skills(job_description)

    resume_skills = parsed_data.get("skills", [])

    skill_comparison = compare_skills(resume_skills, job_details)

    match_score = calculate_match_score(skill_comparison["matched_skills"], job_details)

    suggestions = generate_suggestions(
        parsed_data, job_details, skill_comparison, match_score
    )

    return {
        "parsed_data": parsed_data,
        "job_details": job_details,
        "skill_comparison": skill_comparison,
        "match_score": match_score,
        "suggestions": suggestions,
    }
