# Discord Ban List wrapper for python

Non-official wrapper for [Discord Bans][dbans].

## Installation

just `pip install https://github.com/romangraef/discord_ban_list/archive/master.zip`

## Usage

```python
from discord_ban_list import DiscordBanList
ban_list = DiscordBanList('YOUR_TOKEN')

async def on_something():
    ban_entries = ban_list.check(123456789123456789)
    ban_entry = ban_entries[0]
    print(ban_entry.banned)
    print(ban.user_id)
    print(ban.case_id)
    print(ban.reason)
    print(ban.proof)

async def on_something_two():
    ban_entries = ban_list.check(0, 1, 2, 0)
    # automatically only check 0, 1 and 2
    # we also have client side handling for the 99 users limit
    for entry in ban_entries:
        print(f'{ban.user_id} - {ban.banned}')

```


[dbans]: https://bans.discord.id

