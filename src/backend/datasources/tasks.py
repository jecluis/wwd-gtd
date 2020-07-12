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
from ..sqlite_backend import SQLiteBackend
from ..globals.context import WWDContext
from ..base.task import Task
from .resource import DataResource


def init_backend(backend):

    conn = backend.get_conn(who="tasks backend init")
    cursor = conn.cursor()

    rows = cursor.execute(
    """
        SELECT name from sqlite_master WHERE type='table' AND name='tasks'
    """)

    for r in rows:
        cursor.close()
        return # table has been found
    else:
        print("table not found -- create!")

    cursor.execute("""
        create table if not exists tasks (
            uuid text PRIMARY KEY,
            title text,
            priority integer,
            due text,
            tags text,
            parent text
        )
    """)

    cursor.execute("""
        create table if not exists tasks_extras (
            field text,
            value text,
            task text
        )
    """)

    conn.commit()
    backend.put_conn(who="tasks backend init")

    pass

class TasksDataSource(DataResource):
    
    wwdctx: WWDContext = None
    backend : SQLiteBackend = None

    def __init__(self, wwdctx):
        self.wwdctx = wwdctx
        self.backend = wwdctx.get_data_backend()

        init_backend(self.backend)
        pass

    @classmethod
    def create(cls, wwdctx: WWDContext, title: str):
        return Task.create(wwdctx, title)

    def get(self, uuid=None, title=None):
        pass

    def put(self, task : Task):
        conn = self.backend.get_conn(who="task put")
        cursor = conn.cursor()

        uuid = str(task.uuid)
        title = task.title
        prio = task.priority if task.priority else 0
        due = str(task.due) if task.due else ""
        tags = str(task.tags.uuid) if task.tags else ""
        parent = str(task.parent) if task.parent else ""

        query = """
            INSERT INTO tasks VALUES ('{}', '{}', {}, '{}', '{}', '{}')
        """.format(uuid, title, prio, due, tags, parent)

        print("put task query = {}".format(query))
        cursor.execute(query)

        conn.commit()
        return task

    def rm(self, uuid=None, title=None):
        pass

    def list(self):
        query = """
            SELECT * FROM tasks
        """
        conn = self.backend.get_conn(who="task list")
        cursor = conn.cursor()
        ret_lst = cursor.execute(query)
        conn.close()

        lst = []
        for r in ret_lst:
            print(">> {}".format(r))
            lst.append(r)

        return lst