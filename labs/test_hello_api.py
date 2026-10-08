import asyncio
import httpx
from labs.hello_api import app

def test_root():
    async def request():
        async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url='http://test.local') as client:
            return await client.get('/')
    r = asyncio.run(request())
    assert r.status_code == 200
    assert r.json()["status"] == "ok"
