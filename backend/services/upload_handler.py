from fastapi import UploadFile, HTTPException
import os

# TODO: move shared path/config constants into config.py
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

ALLOWED_TYPES = {
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}


async def validate_and_save_upload(
    file: UploadFile, job_description: str
) -> tuple[str, str]:
    if not job_description or not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    if len(job_description.strip()) < 40:
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
