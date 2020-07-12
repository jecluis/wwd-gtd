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
import uuid as _uuid
from typing import List

from ..globals.context import WWDContext
from .priorities import Priority
from .tags import Tag


class Task:

    wwdctx: WWDContext = None
    uuid: _uuid.UUID = None
    title: str = None
    priority: Priority = None
    due = None
    notes: str = None
    tags: List[Tag] = []
    tags_ctx = None
    children = []
    parent : _uuid.UUID = None

    def __init__(self, wipwd_context: WWDContext):
        self.wipwd_context = wipwd_context        
        self.children = []

    @classmethod
    def create(
            cls,
            wipwd_context: WWDContext,
            title: str,
            prio: Priority = None,
            due=None,
            tags: List[Tag] = None,
            parent: _uuid.UUID = None,
            ctx=None):
        task = cls(wipwd_context)
        task.title = title
        task.prio = prio
        task.due = due
        task.tags = tags
        task.task_ctx = ctx
        task.uuid = _uuid.uuid1()
        task.parent = parent
        return task

    def __str__(self):
        return "{}".format(self.title)
