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
import datetime


def analyze_resume_core(file_path: str, job_description: str):
    extracted_text = extract_text(file_path)

    parsed_data = parse_resume_text(extracted_text)

    job_details = extract_skills(job_description)

    job_skills_groups = categorize_skills(job_details)

    resume_skills = parsed_data.get("skills", [])

    resume_skills_groups = categorize_skills(resume_skills)

    skill_comparison = compare_skills(resume_skills, job_details)

    match_score = calculate_match_score(skill_comparison["matched_skills"], job_details)

    match_summary = build_category_match_summary(
        job_skills_groups, resume_skills_groups
    )

    weighted_match_score = calculate_weighted_match_score(match_summary)

    suggestions = generate_suggestions(
        parsed_data,
        job_details,
        skill_comparison,
        match_score,
        match_summary,
        job_skills_groups,
    )

    analyzed_at = datetime.datetime.now().isoformat()

    return {
        "parsed_data": parsed_data,
        "job_details": job_details,
        "skill_comparison": skill_comparison,
        "match_score": match_score,
        "suggestions": suggestions,
        "job_skills_groups": job_skills_groups,
        "resume_skills_groups": resume_skills_groups,
        "match_summary": match_summary,
        "weighted_match_score": weighted_match_score,
        "analyzed_at": analyzed_at,
    }
