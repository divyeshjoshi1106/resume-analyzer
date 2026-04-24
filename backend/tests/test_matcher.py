from services.matcher import compare_skills, calculate_match_score


def test_compare_skills():
    resume_skills = ["Python", "Python", "Docker"]
    job_skills = ["Docker", "AWS", "Kubernetes"]

    result = compare_skills(resume_skills, job_skills)

    assert result["matched_skills"] == ["Docker"]
    assert result["missing_skills"] == ["AWS", "Kubernetes"]
    assert result["extra_skills"] == ["Python"]
    assert result["matched_skills"].count("Docker") == 1


def test_calculate_match_score():
    resume_skills = ["Python", "Python", "Docker"]
    job_skills = ["Docker", "AWS", "Kubernetes"]

    result = compare_skills(resume_skills, job_skills)
    match_score = calculate_match_score(result["matched_skills"], job_skills)

    assert round(match_score, 2) == 33.33


def test_match_score_empty_job():
    match_score = calculate_match_score([], [])
    assert match_score == 0
