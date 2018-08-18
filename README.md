# Discord Ban List wrapper for python

Non-official wrapper for [Discord bans][dbans].

## Installation

just `pip install https://github.com/romangraef/discord_ban_list/archive/master.zip`

## Usage

```python
from discord_ban_list import DiscordBanList
ban_list = DiscordBanList('YOUR_TOKEN')

async def on_something():
    ban_entry = ban_list.check(123456789123456789)
    print(ban_entry.banned)
    print(ban.user_id)
    print(ban.case_id)
    print(ban.reason)
    print(ban.proof)

```


[dbans]: https://bans.discord.id

