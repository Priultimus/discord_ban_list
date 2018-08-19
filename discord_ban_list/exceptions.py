"""
Module containing exceptions for the discord_ban_list module
"""


class TooManyUsers(Exception):
    """
    Risen if more users than possible are requested.

    """

    def __init__(self, count):
        super(TooManyUsers, self).__init__(
            "You may at most request 99 users at once. 99 < %s" % count)
