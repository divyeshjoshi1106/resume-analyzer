from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_analyze_endpoint_invalid_input():
    response = client.post("/analyze_resume_report")

    assert response.status_code == 422  # missing required fields


def test_analyze_resume_report_invalid_file_type():
    response = client.post(
        "/analyze_resume_report",
        files={"file": ("resume.txt", b"Python Docker", "text/plain")},
        data={"job_description": "Python Docker"},
    )

    assert response.status_code == 400


def test_analyze_resume_report_missing_job_description():
    with open("uploads/CVJoshi.pdf", "rb") as f:
        response = client.post(
            "/analyze_resume_report",
            files={"file": ("CVJoshi.pdf", f, "application/pdf")},
        )

    assert response.status_code == 422


def test_analyze_resume_report_with_real_pdf():
    job_description = (
        "Looking for Python, Docker, Kubernetes, Java, JavaScript, C, C++ ."
    )

    with open("uploads/CVJoshi.pdf", "rb") as f:
        response = client.post(
            "/analyze_resume_report",
            files={"file": ("CVJoshi.pdf", f, "application/pdf")},
            data={"job_description": job_description},
        )

    assert response.status_code == 200

    data = response.json()

    assert "match_score" in data
    assert "summary" in data

    # actual logic checks
    assert "Python" in data["matched_skills"]
    assert "Docker" in data["matched_skills"]
