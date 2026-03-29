import logging

logger = logging.getLogger(__name__)

class TinyFishSession:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def open(self, url: str):
        logger.info(f"[TinyFish] Opening URL: {url}")

    async def click(self, selector: str):
        logger.info(f"[TinyFish] Clicking selector: '{selector}'")

    async def type(self, selector: str, text: str):
        logger.info(f"[TinyFish] Typed '{text}' into '{selector}'")

    async def scroll(self):
        logger.info("[TinyFish] Scrolled down the page.")

    async def wait(self, seconds: int = 1):
        logger.info(f"[TinyFish] Waited for {seconds} seconds.")

    async def upload(self, selector: str, file_path: str):
        logger.info(f"[TinyFish] Uploaded file '{file_path}' into '{selector}'")

    async def extract(self, schema: dict):
        logger.info(f"[TinyFish] Extracting data using schema: {schema}")
        # Returns pseudo data mimicking real extraction payload
        return [
            {
                "title": "AI Traffic Management System",
                "description": "Looking for AI and IoT based smart traffic system",
                "budget": "₹10L - ₹25L",
                "deadline": "2026-04-10",
                "source_url": "https://example.com"
            },
            {
                "title": "Basic Website Development",
                "description": "Simple HTML website required",
                "budget": "₹50K",
                "deadline": "2026-04-05",
                "source_url": "https://example.com"
            }
        ]

class TinyFishClient:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("TinyFish API key missing")
        self.api_key = api_key

    async def start_session(self) -> TinyFishSession:
        logger.info("[TinyFish] Starting new session.")
        # pseudo session (replace with real SDK call)
        return TinyFishSession(self.api_key)
