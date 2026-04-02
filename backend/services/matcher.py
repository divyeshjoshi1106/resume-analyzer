def compare_skills(resume_skills: list[str], job_skills: list[str]):

    skills_dict = {
        "matched_skills": list(set(resume_skills) & set(job_skills)),
        "missing_skills": list(set(job_skills) - set(resume_skills)),
        "extra_skills": list(set(resume_skills) - set(job_skills)),
    }
    return skills_dict
