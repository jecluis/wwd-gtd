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
import flask
from flask_restful import Resource, Api

from backend.globals.context import WWDContext
from backend.globals.config import WWDConfig
from backend.datasources.tasks import TasksDataSource
from backend.dataviews.boxed_tasks import BoxedTasks
from backend.base.task import Task
from backend.base.box import Box
from backend.sqlite_backend import SQLiteBackend

from backend.controllers.task_controller import TaskController


def serve(wwdctx):

    app = flask.Flask('wwd:gtd')
    api = Api(app)

    task_datasource = TasksDataSource(wwdctx)

    api.add_resource(
        TaskController,
        '/tasks',
        resource_class_kwargs={'wwdctx': wwdctx, 'datasource': task_datasource}
    )

    app.run(
        host='0.0.0.0',
        port=31337,
        debug=True)

if __name__ == '__main__':

    print("welcome to our main thing")

    wwdcfg = WWDConfig()
    wwdcfg.set_db_path("./sqlite.db")

    sqlite = SQLiteBackend(wwdcfg)
    wwdctx = WWDContext(wwdcfg)
    wwdctx.set_data_backend(sqlite)
    task_datasource = TasksDataSource(wwdctx)
    task = TasksDataSource.create(wwdctx, "task: foo bar")
    task_datasource.put(task)

    print("created task: {}".format(task))

    print("tasks list:")
    task_datasource.list()

    print("from task controller:")
    task_ctrl = TaskController(wwdctx, task_datasource)
    available_tasks_json = task_ctrl.get()
    print("  available tasks: {}".format(available_tasks_json))

    box = Box.create(wwdctx, "my inbox")
    boxed_tasks = BoxedTasks(wwdctx, box)
    boxed_tasks.add(task)

    print("boxed tasks: {}".format(boxed_tasks.list()))

    serve(wwdctx)

