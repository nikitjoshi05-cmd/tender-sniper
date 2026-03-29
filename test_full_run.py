import traceback
import asyncio
from app.api.routes.agent_routes import full_run

async def main():
    try:
        res = await full_run()
        print("====== FULL RUN OUTPUT ======")
        import json
        print(json.dumps(res, indent=2))
    except Exception as e:
        print("\n=== CRASH TRACEBACK ===")
        traceback.print_exc()

asyncio.run(main())
