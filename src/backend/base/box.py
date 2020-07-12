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

from ..globals.context import WWDContext

class Box:

    uuid: _uuid.UUID = None
    wwdctx: WWDContext = None
    name: str

    def __init__(self, wwdcontext: WWDContext):
        self.wwdctx = wwdcontext
        
    @classmethod
    def create(cls, wwdcontext: WWDContext, name: str):
        box = cls(wwdcontext)
        box.uuid = _uuid.uuid1()
        box.name = name
        return box

    def __str__(self):
        return "box '{}'".format(self.name)
