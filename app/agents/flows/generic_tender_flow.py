import logging

logger = logging.getLogger(__name__)

async def go_to_tenders_section(session):
    """
    Navigates to the tenders listings section of the portal.
    """
    logger.info("Navigating to the tenders section...")
    # Simulate clicking on the navigation menu
    await session.click("a#tenders-link")
    await session.wait(2)
    logger.info("Successfully navigated to the tenders section.")

async def extract_tenders(session) -> list:
    """
    Extracts structured tender data from the current page.
    """
    logger.info("Extracting tenders from the current page...")
    
    # CSS Selectors for the structured data
    schema_dict = {
        "title": "h2.tender-title",
        "description": "div.tender-description",
        "budget": "span.tender-budget",
        "deadline": "span.tender-deadline"
    }
    
    extracted_data = await session.extract(schema_dict)
    logger.info(f"Extracted {len(extracted_data)} tenders.")
    return extracted_data

async def handle_pagination(session) -> bool:
    """
    Clicks the 'Next' button to navigate to the next page.
    Returns True if successful, False if no more pages.
    """
    logger.info("Attempting to navigate to the next page...")
    try:
        await session.scroll()
        await session.click("button.next-page")
        await session.wait(2)
        logger.info("Navigated to the next page successfully.")
        return True
    except Exception as e:
        logger.info(f"No more pages left or failed to navigate: {e}")
        return False
