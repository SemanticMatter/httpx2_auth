import httpx2
import pytest
from pytest_httpx2 import HTTPXMock

import httpx2_auth


@pytest.mark.asyncio
async def test_basic_authentication_send_authorization_header(httpx_mock: HTTPXMock):
    auth = httpx2_auth.Basic("test_user", "test_pwd")

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Basic dGVzdF91c2VyOnRlc3RfcHdk",
        },
    )

    async with httpx2.AsyncClient() as client:
        await client.get("https://authorized_only", auth=auth)
