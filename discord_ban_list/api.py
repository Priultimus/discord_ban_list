from asyncio import Lock
from typing import Union

from aiohttp import ClientSession

from .result import Ban, NoBan, BanABC

CHECK_URL = 'https://bans.discord.id/api/check.php'


class DiscordBanList(object):
    __slots__ = ('token', '_client', '_client_lock')

    def __init__(self, token: str, _client: ClientSession = None):
        self.token = token
        self._client = _client
        self._client_lock = Lock()

    async def login(self):
        await self._guarantee_client()

    async def check(self, user_id: Union[int, str]) -> BanABC:
        resp = await self._get('{base}?user_id={user_id}'.format(base=CHECK_URL, user_id=user_id))
        if resp['banned'] == "0":
            return NoBan(user_id)
        return Ban(user_id, resp['reason'], resp['case_id'], resp['proof'])

    async def _get(self, url):
        async with self._client.get(url,
                                    headers={'Authorization': self.token}) as resp:
            resp.raise_for_status()
            return await resp.json(content_type=None)

    async def _guarantee_client(self):
        if self._client is None:
            async with self._client_lock:
                if self._client is None:
                    self._client = ClientSession()
        return self._client
