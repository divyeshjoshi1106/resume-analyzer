import json
import os
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # services/
BACKEND_DIR = os.path.dirname(BASE_DIR)  # backend/

skills_path = os.path.join(BACKEND_DIR, "app", "data", "skill_categories.json")

with open(skills_path, "r", encoding="utf-8") as f:
    SKILLS_CATEGORIES = json.load(f)


def categorize_skills(skills: list[str]):
    result = defaultdict(list)
    for skill in skills:
        skill_lower = skill.lower()
        found = False
        for category, category_skills in SKILLS_CATEGORIES.items():
            if skill_lower in [s.lower() for s in category_skills]:
                result[category].append(skill)
                found = True
                break
        if not found:
            result["other"].append(skill)
    return dict(result)
