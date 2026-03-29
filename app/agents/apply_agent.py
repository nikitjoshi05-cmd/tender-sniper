from app.core.config import settings
from app.core.tinyfish import TinyFishClient
from app.agents.flows.application_flow import (
    open_tender_page,
    click_apply_button,
    fill_application_form,
    submit_application
)


class ApplyAgent:
    def __init__(self):
        # We assume the user has set TINYFISH_API_KEY in .env
        self.client = TinyFishClient(settings.TINYFISH_API_KEY)

    async def apply_to_tender(self, tender_url: str, company: dict):
        session = await self.client.start_session()

        print("Opening tender page...")
        await open_tender_page(session, tender_url)

        print("Clicking apply...")
        await click_apply_button(session)

        print("Filling form...")
        await fill_application_form(session, company)

        print("Submitting application...")
        await submit_application(session)

        return {
            "status": "applied",
            "tender_url": tender_url
        }
