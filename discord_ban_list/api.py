"""
Central API module. Most action taskes place here
"""

from asyncio import Lock
from typing import Union

from aiohttp import ClientSession

from .result import Ban, NoBan, BanABC

CHECK_URL = 'https://bans.discord.id/api/check.php'


class DiscordBanList(object):
    """
    API wrapper for the ban list with a given token.
    """

    __slots__ = ('token', '_client', '_client_lock')

    def __init__(self, token: str, _client: ClientSession = None):
        """

        :param token: the generated token for the ban list. see http://bans.discord.id/
        :param _client: pass a value here if you want to use a shared client.
                        Leave empty to autoinitialize
        """
        self.token = token
        self._client = _client
        self._client_lock = Lock()

    async def login(self):
        """
        Login the client in. E.g. check the client session is loaded.
        """
        await self._guarantee_client()

    async def check(self, user_id: Union[int, str]) -> BanABC:
        """
        Check if a user is banned on DBans

        :param user_id: id of the user to be checked
        :return: a :class:`BanABC`
        """
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
