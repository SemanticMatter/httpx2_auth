import httpx2
import pytest
from pytest_httpx2 import HTTPXMock

import httpx2_auth


@pytest.mark.asyncio
async def test_header_api_key_is_sent_in_x_api_key_by_default(httpx_mock: HTTPXMock):
    auth = httpx2_auth.HeaderApiKey("my_provided_api_key")

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={"X-API-Key": "my_provided_api_key"},
    )

    async with httpx2.AsyncClient() as client:
        await client.get("https://authorized_only", auth=auth)


@pytest.mark.asyncio
async def test_query_api_key_is_sent_in_api_key_by_default(httpx_mock: HTTPXMock):
    auth = httpx2_auth.QueryApiKey("my_provided_api_key")

    httpx_mock.add_response(url="https://authorized_only?api_key=my_provided_api_key", method="GET")

    async with httpx2.AsyncClient() as client:
        await client.get("https://authorized_only", auth=auth)


@pytest.mark.asyncio
async def test_header_api_key_can_be_sent_in_a_custom_field_name(httpx_mock: HTTPXMock):
    auth = httpx2_auth.HeaderApiKey("my_provided_api_key", "X-API-HEADER-KEY")

    httpx_mock.add_response(
        url="https://authorized_only",
        method="GET",
        match_headers={"X-API-HEADER-KEY": "my_provided_api_key"},
    )

    async with httpx2.AsyncClient() as client:
        await client.get("https://authorized_only", auth=auth)


@pytest.mark.asyncio
async def test_query_api_key_can_be_sent_in_a_custom_field_name(httpx_mock: HTTPXMock):
    auth = httpx2_auth.QueryApiKey("my_provided_api_key", "X-API-QUERY-KEY")

    httpx_mock.add_response(
        url="https://authorized_only?X-API-QUERY-KEY=my_provided_api_key", method="GET"
    )

    async with httpx2.AsyncClient() as client:
        await client.get("https://authorized_only", auth=auth)
