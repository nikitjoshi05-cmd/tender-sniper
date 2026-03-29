def match_tender(tender: dict, company: dict) -> dict:
    score = 0
    reasons = []

    # Budget match
    if company["min_budget"] <= tender["budget"] <= company["max_budget"]:
        score += 1
        reasons.append("Budget is within range")

    # Skill match
    matched_skills = [
        skill for skill in company["skills"]
        if skill.lower() in tender["description"].lower()
    ]

    if matched_skills:
        score += 1
        reasons.append(f"Matched skills: {', '.join(matched_skills)}")

    # Decision threshold
    is_match = score >= 2

    return {
        "is_match": is_match,
        "score": score,
        "reasons": reasons
    }
