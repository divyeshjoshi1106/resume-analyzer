from services.suggester import generate_suggestions


def test_generate_suggestions():
    skill_comparison = {
        "matched_skills": ["CI/CD", "Docker", "Jenkins"],
        "missing_skills": [
            "AWS",
            "Ansible",
            "Confluence",
            "Jira",
            "Kubernetes",
            "Terraform",
        ],
        "extra_skills": ["Python", "Java", "FastAPI"],
    }

    match_score = 33.33

    category_match_summary = {
        "devops": {"matched": 3, "required": 6},
        "cloud": {"matched": 0, "required": 1},
        "tools_collaboration": {"matched": 0, "required": 2},
    }

    job_skills_groups = {
        "devops": ["Ansible", "CI/CD", "Docker", "Jenkins", "Kubernetes", "Terraform"],
        "cloud": ["AWS"],
        "tools_collaboration": ["Confluence", "Jira"],
    }

    result = generate_suggestions(
        skill_comparison,
        match_score,
        category_match_summary,
        job_skills_groups,
    )

    assert result["match_level"] == "Moderate"
    assert "moderate match" in result["summary"].lower()
    assert "AWS" in result["improvements"]
    assert "Kubernetes" in result["improvements"]
    assert "DevOps" in result["category_feedback"]
