from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")


@app.get("/health")
def health():
    print("health endpoint")
    return {"status": "ok"}


@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
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
