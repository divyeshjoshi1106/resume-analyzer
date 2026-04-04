def format_skill_list(skills):
    if not skills:
        return ""

    if len(skills) == 1:
        return skills[0]
    if len(skills) == 2:
        return f"{skills[0]} and {skills[1]}"
    return f"{', '.join(skills[:-1])}, and {skills[-1]}"


def generate_suggestions(
    parsed_data, job_details, skill_comparison, match_score
) -> dict:
    matched = skill_comparison.get("matched_skills", [])[:5]
    missing = skill_comparison.get("missing_skills", [])[:5]

    if match_score <= 30:
        summary = "This resume has a low match with the job requirements."
    elif match_score <= 60:
        summary = "This resume has a moderate match with the job requirements."
    else:
        summary = "This resume has a strong match with the job requirements."

    if matched:
        strengths = f"You have relevant experience with {format_skill_list(matched)}."
    else:
        strengths = "No strong skill matches found for this role."

    if missing:
        improvements = f"Consider adding or highlighting experience with {format_skill_list(missing)} if applicable."
    else:
        improvements = "Your resume covers most of the required skills."

    return {"summary": summary, "strengths": strengths, "improvements": improvements}
