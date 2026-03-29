import logging
from typing import List, Dict, Any

from app.core.config import settings
from app.core.tinyfish import TinyFishClient
from app.agents.flows.generic_tender_flow import (
    go_to_tenders_section,
    extract_tenders,
    handle_pagination
)

# Set up logging for the agent
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ScrapeAgent:
    """
    Agent responsible for scraping tender information using TinyFish.
    """
    def __init__(self):
        # Initialize TinyFish explicitly using the API Key read from standard settings
        self.client = TinyFishClient(settings.TINYFISH_API_KEY)

    async def run(self, url: str) -> List[Dict[str, Any]]:
        """
        Executes the web scraping workflow.
        """
        logger.info(f"Starting ScrapeAgent run for URL: {url}")
        all_tenders = []
        
        # 1. Start the session context using the client
        session = await self.client.start_session()
        
        # 2. Open the given URL
        await session.open(url)
        
        # 3. Wait for page load
        await session.wait(3) 
        
        # 4. Navigate to tender listings
        await go_to_tenders_section(session)
        
        # 5. Handle basic pagination (at least 2 pages)
        pages_to_scrape = 2
        for page in range(1, pages_to_scrape + 1):
            logger.info(f"--- Scraping Page {page} ---")
            
            # Extract structured tender data
            page_tenders = await extract_tenders(session)
            all_tenders.extend(page_tenders)
            
            # Navigate to the next page if this isn't the last iteration
            if page < pages_to_scrape:
                has_next = await handle_pagination(session)
                if not has_next:
                    break
                    
        logger.info(f"ScrapeAgent run completed. Total tenders extracted: {len(all_tenders)}")
        return all_tenders
