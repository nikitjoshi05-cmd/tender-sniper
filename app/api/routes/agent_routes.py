from fastapi import APIRouter
from app.agents.scrape_agent import ScrapeAgent
from app.agents.apply_agent import ApplyAgent
from app.services.parser_service import parse_tender
from app.services.matching_service import match_tender
from app.services.llm_service import generate_reasoning

router = APIRouter()

@router.get("/run")
async def run_agent(url: str = "https://example-tenders.gov"):
    """
    Runs the ScrapeAgent for the specified URL and returns the extracted tenders.
    """
    agent = ScrapeAgent()
    extracted_data = await agent.run(url)
    return {
        "status": "success",
        "url": url,
        "count": len(extracted_data),
        "data": extracted_data
    }

@router.get("/analyze")
async def analyze_tenders():
    try:
        agent = ScrapeAgent()
        raw_tenders = await agent.run("https://example.com")

        company = {
            "name": "Tech Solutions Pvt Ltd",
            "skills": ["AI", "IoT", "Web Development"],
            "min_budget": 500,
            "max_budget": 5000000
        }

        results = []

        for tender in raw_tenders:
            parsed = parse_tender(tender)
            match = match_tender(parsed, company)
            
            # Now awaited dynamically through the new IO-bound integration
            reasoning = await generate_reasoning(parsed, company, match)

            results.append({
                "tender": parsed,
                "match": match,
                "reasoning": reasoning
            })

        return {
            "status": "success",
            "total_tenders": len(results),
            "results": results
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}

@router.get("/full-run")
async def full_run():
    try:
        scrape_agent = ScrapeAgent()
        apply_agent = ApplyAgent()
        
        raw_tenders = await scrape_agent.run("https://example.com")

        company = {
            "name": "Tech Solutions Pvt Ltd",
            "skills": ["AI", "IoT", "Web Development"],
            "min_budget": 500,
            "max_budget": 5000000
        }

        results = []

        for tender in raw_tenders:
            parsed = parse_tender(tender)
            match = match_tender(parsed, company)
            
            reasoning = await generate_reasoning(parsed, company, match)

            if match["is_match"]:
                application = await apply_agent.apply_to_tender(
                    parsed["source_url"], company
                )
            else:
                application = {"status": "skipped"}

            results.append({
                "tender": parsed,
                "match": match,
                "reasoning": reasoning,
                "application": application
            })

        return {"results": results}

    except Exception as e:
        return {"error": str(e)}
