from typing import Any, Dict, Optional
from aiohttp.client_exceptions import ClientResponseError
import logging
import aiohttp
from aiohttp.typedefs import LooseHeaders
from multidict import CIMultiDict

from src.logger import correlation_id_ctx, logger

from conf.config import settings


class ClientSessionWithCorrId(aiohttp.ClientSession):
    def _prepare_headers(self, headers: Optional[LooseHeaders]) -> CIMultiDict[str]:
        headers = super()._prepare_headers(headers)

        correlation_id = correlation_id_ctx.get()
        headers['X-Correlation-Id'] = correlation_id

        return headers


async def post_to_server(url, params=None):
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        try:
            async with session.post(
                f'{settings.TINDER_BACKEND_HOST}/{url}',
                json=params,
            ) as response:
                response.raise_for_status()
                data = await response.json()
                return True, data
        except ClientResponseError as e:
            logging.error(e)
            return False, e


async def get_from_server(url, params=None):
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector()
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        try:
            async with session.get(
                f'{settings.TINDER_BACKEND_HOST}/{url}',
                json=params,
            ) as response:
                response.raise_for_status()
                data = await response.json()
                return True, data
        except ClientResponseError as e:
            return False, e
