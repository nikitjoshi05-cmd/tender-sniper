import traceback
import asyncio
from app.api.routes.agent_routes import run_agent

async def main():
    try:
        from app.core.config import settings
        print("Settings API Key:", repr(settings.TINYFISH_API_KEY))
        
        # Test the endpoint routing directly
        print("Testing run_agent...")
        res = await run_agent()
        print("Result:", res)
    except Exception as e:
        print("\n=== CRASH TRACEBACK ===")
        traceback.print_exc()

asyncio.run(main())
