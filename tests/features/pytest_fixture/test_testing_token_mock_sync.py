import httpx2
from pytest_httpx2 import HTTPXMock

import httpx2_auth


def test_token_mock(token_cache_mock, httpx_mock: HTTPXMock):
    auth = httpx2_auth.OAuth2Implicit("https://provide_token")

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={
            "Authorization": "Bearer 2YotnFZFEjr1zCsicMWpAA",
        },
    )

    with httpx2.Client() as client:
        client.get("https://authorized_only", auth=auth)
