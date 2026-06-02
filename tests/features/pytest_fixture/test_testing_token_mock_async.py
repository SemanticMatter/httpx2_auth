import httpx2
import pytest
from pytest_httpx2 import HTTPXMock

import httpx2_auth


@pytest.mark.asyncio
async def test_token_mock(token_cache_mock, httpx_mock: HTTPXMock):
    auth = httpx2_auth.OAuth2Implicit("https://provide_token")

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Bearer 2YotnFZFEjr1zCsicMWpAA",
        },
    )

    async with httpx2.AsyncClient() as client:
        await client.get("https://authorized_only", auth=auth)
