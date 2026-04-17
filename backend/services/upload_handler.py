from fastapi import UploadFile
from app.config import ALLOWED_TYPES, MIN_JOB_DESCRIPTION_LENGTH, UPLOAD_DIR
import os


async def validate_and_save_upload(
    file: UploadFile, job_description: str
) -> tuple[str, str]:
    if not job_description or not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    if len(job_description.strip()) < MIN_JOB_DESCRIPTION_LENGTH:
        raise ValueError("Job description is too short. Please provide more details.")

    if not file.filename:
        raise ValueError("No file was uploaded.")

    if file.content_type not in ALLOWED_TYPES:
        raise ValueError("Only PDF and DOCX files are allowed.")

    content = await file.read()

    if not content:
        raise ValueError("Uploaded file is empty.")

    safe_filename = os.path.basename(file.filename)
    file_path = os.path.join(UPLOAD_DIR, safe_filename)

    print(file_path)

    with open(file_path, "wb") as f:
        f.write(content)

    return (job_description.strip(), file_path)
