def build_analysis_report(analysis_result: dict):
    return {
        "candidate_name": analysis_result["resume_details"]["name"],
        "match_level": analysis_result["suggestions"]["match_level"],
        "match_score": analysis_result["match_score"],
        "weighted_match_score": analysis_result["weighted_match_score"],
        "matched_skills": analysis_result["skill_comparison"]["matched_skills"],
        "missing_skills": analysis_result["skill_comparison"]["missing_skills"],
        "summary": analysis_result["suggestions"]["summary"],
        "top_improvements": analysis_result["suggestions"]["improvements"],
        "category_feedback": analysis_result["suggestions"]["category_feedback"],
        "analyzed_at": analysis_result["analyzed_at"],
    }
