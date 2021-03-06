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
from typing import Dict, List
import uuid

from ..globals.context import WWDContext
from ..base.box import Box
from ..base.task import Task


class BoxedTasks:

    wwdctx : WWDContext = None
    box : Box = None
    tasks : Dict[uuid.UUID, Task] = {}

    def __init__(self, wwdctx: WWDContext, box: Box):
        self.wwdctx = wwdctx

    def add(self, task: Task):
        if task.uuid in self.tasks:
            raise LookupError("task already tracked")

        self.tasks[task.uuid] = task

    def list(self) -> List[Task]:
        lst = [t for t in self.tasks.values()]
        return lst


