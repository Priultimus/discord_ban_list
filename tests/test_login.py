import os
from asyncio import get_event_loop
from unittest import TestCase

from discord_ban_list import DiscordBanList


async def a_test_valid_login():
    ban_list = DiscordBanList(os.environ['token'])
    await ban_list.login()
    ban = await ban_list.check(123)
    assert not ban.banned


async def a_test_banned():
    user = 123456789123456789
    ban_list = DiscordBanList(os.environ['token'])
    await ban_list.login()
    ban = await ban_list.check(user)
    assert ban.banned
    assert ban.user_id == user
    assert ban.case_id == 9999
    assert ban.reason
    assert ban.proof


class TestSomething(TestCase):
    def test_not_banned(self):
        get_event_loop().run_until_complete(a_test_valid_login())

    def test_banned(self):
        get_event_loop().run_until_complete(a_test_banned())
