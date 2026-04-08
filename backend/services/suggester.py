def format_skill_list(skills):
    if not skills:
        return ""

    if len(skills) == 1:
        return skills[0]
    if len(skills) == 2:
        return f"{skills[0]} and {skills[1]}"
    return f"{', '.join(skills[:-1])}, and {skills[-1]}"


def generate_suggestions(
    parsed_data,
    job_details,
    skill_comparison,
    match_score,
    match_summary,
    job_skills_groups,
) -> dict:
    matched = skill_comparison.get("matched_skills", [])
    missing = skill_comparison.get("missing_skills", [])

    if match_score <= 30:
        summary = "This resume currently has a low match with the job requirements."
        score_feedback = "The resume may need significant tailoring for this role, especially around the missing technical requirements."
    elif match_score <= 60:
        summary = "This resume shows a moderate match with the job requirements."
        score_feedback = "The resume has some relevant alignment, but could be strengthened by emphasizing more of the required tools and technologies."
    else:
        summary = "This resume shows a strong match with the job requirements."
        score_feedback = "The resume is already well aligned with the role and may only need minor tailoring."

    if matched:
        strengths = f"Your profile already aligns with the role in areas such as {format_skill_list(matched)}."
        highlight_advice = f"Highlight your existing {format_skill_list(matched)} experience more clearly, as these already align with the role."
    else:
        strengths = "No strong skill matches found for this role."
        highlight_advice = "No directly aligned skills were found for this role. Consider emphasizing transferable technical experience and adding relevant role-specific skills if applicable."  # if you have worked with them?.

    if missing:
        improvements = f"To improve alignment with this role, consider adding or highlighting experience with {format_skill_list(missing)} if applicable."
    else:
        improvements = "Your resume covers most of the required skills."

    category_feedback = generate_category_feedback(
        match_summary, job_skills_groups, missing
    )

    return {
        "summary": summary,
        "strengths": strengths,
        "improvements": improvements,
        "highlight_advice": highlight_advice,
        "score_feedback": score_feedback,
        "category_feedback": category_feedback,
    }


# TODO
def generate_category_feedback(match_summary, job_skills_groups, missing_skills):
    best_category = None
    best_missing_skills = []
    highest_missing_count = 0
    for category, category_data in match_summary.items():
        matched = category_data["matched"]
        required = category_data["required"]

        missing_count = required - matched

        if missing_count <= 0:
            continue

        category_job_skills = job_skills_groups.get(category, [])

        missing_in_this_category = []

        for skill in category_job_skills:
            if skill in missing_skills:
                missing_in_this_category.append(skill)

        if len(missing_in_this_category) > highest_missing_count:
            best_category = category
            best_missing_skills = missing_in_this_category
            highest_missing_count = len(missing_in_this_category)

    if best_category is None:
        return (
            "Your profile aligns reasonably well across the main required categories."
        )

    category_display = format_category_name(best_category)

    if best_missing_skills:
        return f"The biggest gap is in {category_display}-related skills, especially {format_skill_list(best_missing_skills)}."
    else:
        return f"The biggest gap is in {category_display}-related skills."


def format_category_name(category):
    if category == "devops":
        return "DevOps"
    elif category == "tools_collaboration":
        return "tools and collaboration"
    elif category == "data_ai":
        return "data and AI"
    else:
        return category.replace("_", " ")
