def extract_budget(budget_str: str) -> float:
    if not budget_str:
        return 0.0

    # Extract digits from string like "₹10L - ₹25L"
    digits = ''.join(filter(str.isdigit, budget_str))
    return float(digits) if digits else 0.0

def parse_tender(raw_tender: dict) -> dict:
    return {
        "title": raw_tender.get("title", "").strip(),
        "description": raw_tender.get("description", "").strip(),
        "budget": extract_budget(raw_tender.get("budget")),
        "deadline": raw_tender.get("deadline"),
        "source_url": raw_tender.get("source_url", "")
    }
