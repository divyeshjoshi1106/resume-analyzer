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


def build_category_match_summary(job_skills_groups, resume_skills_groups):
    category_match = {}

    for category, category_skills in job_skills_groups.items():
        required_skills = category_skills
        resume_skills = resume_skills_groups.get(category, [])

        match_count = len(
            set(s.lower() for s in resume_skills)
            & set(s.lower() for s in required_skills)
        )

        required_count = len(required_skills)

        category_match[category] = {"matched": match_count, "required": required_count}

    return category_match
