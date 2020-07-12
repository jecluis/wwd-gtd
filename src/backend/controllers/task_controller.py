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
from flask_restful import Resource
import json

from ..globals.context import WWDContext
from ..datasources.tasks import TasksDataSource



class TaskController(Resource):

    ctx: WWDContext = None
    datasource: TasksDataSource = None

    def __init__(self, wwdctx: WWDContext, datasource: TasksDataSource):
        self.ctx = wwdctx
        self.datasource = datasource

    def get(self):
        lst = self.datasource.list()
        fields = ('uuid', 'title', 'prio', 'due', 'tags', 'parent')
        task_lst = []
        for task in lst:
            d = dict(zip(fields, task))
            # print("task_controller >> get = {}".format(d))
            task_lst.append(d)
        return task_lst


    