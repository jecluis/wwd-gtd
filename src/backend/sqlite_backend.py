#!/usr/bin/python3

# Copyright (C) 2020  Joao Eduardo Luis <joao@wipwd.org>
#
# This file is part of WIP:WD's Getting Things Done (wwd-gtd). 
# wwd-gtd is free software: you can redistribute it and/or modify it under the
# terms of the EUROPEAN UNION PUBLIC LICENSE v1.2, as published by the
# European Comission.
#
# wwd-gtd is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the EUROPEAN UNION PUBLIC LICENSE for more
# details.
#
# You should have received a copy of the EUROPEAN UNION PUBLIC LICENSE v1.2
# along with wwd-gtd.  If not, see
#   https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
#
# This text has been cordially ripped off of the GNU's GPL license header,
# and adapted to our purposes.
#

import sqlite3
from threading import Lock
from .globals.config import WWDConfig

class SQLiteBackend:

    conn = None
    config: WWDConfig = None
    lock: Lock = Lock()

    class Connection:
        whoami: str = None
        conn = None
        lock: Lock = None
        cursor_inst = None
        
        def __init__(self, path: str, lock: Lock, who: str = ""):
            self.conn = sqlite3.connect(path)
            if who:
                self.whoami = who
            assert lock.locked()
            self.lock = lock
            print("start connection for {}".format(self.whoami))

        def cursor(self):
            if not self.cursor_inst:
                self.cursor_inst = self.conn.cursor()
            return self.cursor_inst

        def commit(self):
            self.conn.commit()
            self.cursor_inst = None

        def close(self):
            print("close connection for {}".format(self.whoami))
            assert self.conn
            del self

        def __del__(self):
            print("destroy connection for {}".format(self.whoami))
            assert self.lock.locked()
            self.conn.commit()
            self.conn.close()
            self.lock.release()

    def __init__(self, wwdconfig):
        db_path = wwdconfig.get_db_path()
        if not db_path:
            raise IOError("db path not specified")
        self.config = wwdconfig

    def get_conn(self, who=""):
        print("lock acquire {}".format(who))
        self.lock.acquire()
        return SQLiteBackend.Connection(self.config.db_path, self.lock, who=who)