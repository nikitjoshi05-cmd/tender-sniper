async def open_tender_page(session, tender_url: str):
    await session.open(tender_url)
    await session.wait()


async def click_apply_button(session):
    await session.click("button.apply")  # update selector
    await session.wait()


async def fill_application_form(session, company):
    await session.type("input[name='company_name']", company["name"])
    await session.type("textarea[name='experience']", "We have 5+ years experience in AI/IoT projects")

    # Example checkbox
    await session.click("input[name='compliance']")

    # File upload (if supported)
    try:
        await session.upload("input[type='file']", "company_profile.pdf")
    except Exception as e:
        print(f"File upload skipped: {e}")


async def submit_application(session):
    await session.click("button.submit")
    await session.wait()
