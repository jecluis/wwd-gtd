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
from .config import WWDConfig
from ..sqlite_backend import SQLiteBackend

class WWDContext:

    config: WWDConfig = None
    data_backend: SQLiteBackend = None

    def __init__(self, cfg):
        self.config = cfg

    def set_data_backend(self, backend):
        self.data_backend = backend

    def get_data_backend(self):
        return self.data_backend