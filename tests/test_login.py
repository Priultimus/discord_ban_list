import os
from asyncio import get_event_loop
from unittest import TestCase

from discord_ban_list import DiscordBanList, TooManyUsers


async def a_test_valid_login():
    ban_list = DiscordBanList(os.environ['token'])
    await ban_list.login()
    ban = (await ban_list.check(123))[0]
    assert not ban.banned


async def a_test_banned():
    user = 123456789123456789
    ban_list = DiscordBanList(os.environ['token'])
    await ban_list.login()
    ban = (await ban_list.check(user))[0]
    assert ban.banned
    assert ban.user_id == user
    assert ban.case_id == 9999
    assert ban.reason
    assert ban.proof


async def a_test_multiple_bans():
    ban_list = DiscordBanList(os.environ['token'])
    await ban_list.login()
    bans = await ban_list.check(
        0,
        1,
        2,
        123456789123456789,
    )
    for ban in bans:
        if ban.user_id == 123456789123456789:
            assert ban.banned
            assert ban.case_id == 9999
            assert ban.proof
            assert ban.reason
        else:
            assert not ban.banned
    assert len(bans) == 4


async def a_test_no_ids_provided():
    ban_list = DiscordBanList(os.environ['token'])
    await ban_list.login()
    bans = await ban_list.check()
    assert bans == []


async def a_test_id_de_duplication():
    ban_list = DiscordBanList(os.environ['token'])
    await ban_list.login()
    bans = await ban_list.check(*([123456789123456789] * 100 + [0] * 100))
    for ban in bans:
        if ban.user_id == 123456789123456789:
            assert ban.banned
            assert ban.case_id == 9999
            assert ban.proof
            assert ban.reason
        else:
            assert not ban.banned
    assert len(bans) == 2


async def a_test_too_many_ids_provided():
    ban_list = DiscordBanList(os.environ['token'])
    await ban_list.login()
    try:
        await ban_list.check(*list(range(1000)))
    except TooManyUsers:
        return
    assert False


class TestSomething(TestCase):
    def test_valid_login(self):
        get_event_loop().run_until_complete(a_test_valid_login())

    def test_banned(self):
        get_event_loop().run_until_complete(a_test_banned())

    def test_multiple_bans(self):
        get_event_loop().run_until_complete(a_test_multiple_bans())

    def test_no_ids_provided(self):
        get_event_loop().run_until_complete(a_test_no_ids_provided())

    def test_id_de_duplication(self):
        get_event_loop().run_until_complete(a_test_id_de_duplication())

    def test_too_many_ids_provided(self):
        get_event_loop().run_until_complete(a_test_too_many_ids_provided())
