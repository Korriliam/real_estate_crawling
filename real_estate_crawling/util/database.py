from __future__ import unicode_literals
# -*- coding: utf-8 -*-

from django.db import (
    connections, connection
)

def check_connection():
    """
    Aims to check if the connection is still alive.
    If not so, we coerce django to reconnect, and
    so avoiding errors such "(2006, MySQL server
    has gone away)"
    """
    if connection.connection and not connection.is_usable():
        del connections._connections.default
