import os
from dotenv import load_dotenv

load_dotenv()

# Base paths
APP_DIR = os.path.dirname(__file__)
BACKEND_DIR = os.path.abspath(os.path.join(APP_DIR, ".."))

# Environment-based configs
UPLOAD_DIR = os.getenv("UPLOAD_DIR", os.path.join(BACKEND_DIR, "uploads"))
MIN_JOB_DESCRIPTION_LENGTH = int(os.getenv("MIN_JOB_DESC_LENGTH", 40))

# Make sure uploads folder exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Allowed upload types
ALLOWED_TYPES = {
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}

# Scoring
CATEGORY_WEIGHTS = {
    "devops": 0.4,
    "cloud": 0.3,
    "tools_collaboration": 0.1,
    "backend": 0.2,
    "data_ai": 0.1,
}
