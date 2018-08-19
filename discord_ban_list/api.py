"""
Central API module. Most action taskes place here
"""

from asyncio import Lock
from typing import Union, List

from aiohttp import ClientSession

from .exceptions import TooManyUsers
from .result import BanABC

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

    async def check(self, *user_ids: Union[int, str]) -> List[BanABC]:
        """
        Check if some users are banned on DBans

        :param user_ids: ids of the users to be checked
        :return: a list of :class:`BanABC`
        """
        user_ids = list(set(user_ids))
        if len(user_ids) < 1:
            return []
        if len(user_ids) > 99:
            raise TooManyUsers(len(user_ids))
        resp = await self._get(CHECK_URL + '?' + '&'.join('user_id=' +
                                                          str(user_id) for user_id in user_ids))
        return [BanABC.parse(ban) for ban in resp]

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
