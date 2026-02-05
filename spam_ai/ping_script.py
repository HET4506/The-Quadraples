import httpx
import asyncio
import os

# Get URL from env or default to your Render URL
URL = os.getenv("RENDER_URL", "https://your-service-name.onrender.com")

async def stay_awake():
    print(f"Pinging {URL} to stay awake...")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{URL}/")
            print(f"Status: {response.status_code}")
    except Exception as e:
        print(f"Ping failed: {e}")

if __name__ == "__main__":
    asyncio.run(stay_awake())
