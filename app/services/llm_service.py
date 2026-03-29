import logging
from openai import AsyncOpenAI
from app.core.config import settings

logger = logging.getLogger(__name__)

# Initialize client only if we have an API key to prevent crashes natively on boot-up
client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY) if settings.OPENAI_API_KEY and settings.OPENAI_API_KEY != "your_openai_api_key_here" else None

async def generate_reasoning(tender: dict, company: dict, match: dict) -> str:
    """
    Calls the OpenAI API to evaluate the tender against the company profile.
    If no API key is set, falls back to the static rule-based generator.
    """
    if not client:
        return _fallback_reasoning(tender, company, match)
        
    logger.info(f"Generating LLM reasoning for tender: {tender['title']}")
    
    prompt = f"""
You are an expert AI Tender Analyst. Evaluate the following tender for the company.

Company Profile:
Name: {company['name']}
Skills: {', '.join(company['skills'])}
Budget Range: {company['min_budget']} to {company['max_budget']}

Tender Details:
Title: {tender['title']}
Description: {tender.get('description', 'N/A')}
Budget: {tender.get('budget', 'N/A')}
Deadline: {tender.get('deadline', 'N/A')}

Rule-based Match Result: {match['is_match']}
Rule-based Score: {match['score']}

Write a 2-3 sentence reasoning explaining why this is or isn't a strong match. Provide a clear recommendation on whether the company should apply based on their exact skills format and budget expectations.
"""
    
    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a direct, professional AI business operations analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"LLM Reasoning failed: {e}")
        return _fallback_reasoning(tender, company, match)


def _fallback_reasoning(tender: dict, company: dict, match: dict) -> str:
    """Fallback static reasoning if OpenAI is unavailable."""
    if not match["is_match"]:
        return (
            f"[Fallback] This tender '{tender['title']}' is not a strong match "
            "based on current budget or required skills."
        )

    reasons_text = "\n".join([f"- {r}" for r in match["reasons"]])

    return f"Tender: {tender['title']}\n\n[Fallback] This is a strong match for your company.\n\nReasons:\n{reasons_text}\n\nRecommendation: Proceed with application."
