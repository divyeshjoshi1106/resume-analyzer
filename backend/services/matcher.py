from app.config import CATEGORY_WEIGHTS


def compare_skills(resume_skills: list[str], job_skills: list[str]):

    skills_dict = {
        "matched_skills": list(set(resume_skills) & set(job_skills)),
        "missing_skills": list(set(job_skills) - set(resume_skills)),
        "extra_skills": list(set(resume_skills) - set(job_skills)),
    }

    for skill_list in skills_dict.values():
        skill_list.sort()

    return skills_dict


def calculate_match_score(matched_skills: list[str], job_skills: list[str]):
    try:
        match_score = round((len(matched_skills) / len(job_skills)) * 100, 2)
    except ZeroDivisionError:
        match_score = 0
    return match_score


def calculate_weighted_match_score(category_match_summary: dict):
    weighted_sum = 0
    used_weight_sum = 0
    for category, category_data in category_match_summary.items():
        if category not in CATEGORY_WEIGHTS:
            continue

        matched = category_data["matched"]
        required = category_data["required"]

        if required == 0:
            continue

        ratio = matched / required
        weight = CATEGORY_WEIGHTS[category]

        weighted_sum += ratio * weight
        used_weight_sum += weight

    if used_weight_sum == 0:
        return 0.0

    return round((weighted_sum / used_weight_sum) * 100, 2)
