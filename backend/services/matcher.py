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
