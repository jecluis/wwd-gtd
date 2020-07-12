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
import uuid

from box import Box
from task import Task
from ..globals.context import WWDContext
from errors import PipelineException
import yaml
import itertools


class Pipeline:

    class Node:
        def __init__(self, wwdcontext: WWDContext, box: Box, prev, nxt):
            self.wwdctx = wwdcontext
            self.id = uuid.uuid1()
            self.box = box
            self.prev = prev
            self.nxt = nxt

    def __init__(self, wwdcontext: WWDContext):
        self.uuid = uuid.uuid1()
        self.wwdctx = wwdcontext
        self.name = None
        self.first = None
        self.last = None
        self.nodes = []

    def parse(self, cfg_input):

        config = yaml.load(cfg_input)

        """
        config
        ------
        name: My Pipeline
        boxes:
            - Inbox
            - Next
            - In Progress
            - Done
        """

        if 'name' not in config:
            raise PipelineException("pipeline requires a 'name' to be set")
        self.name = config['name']
        if 'boxes' in config:
            prevs, boxes, nexts = itertools.tee(config['boxes'], 3)
            # start 'previous elements' iterator with a None
            prevs = itertools.chain([None], prevs)
            # end 'next elements' iterator with a None
            nexts = itertools.chain(itertools.islice(nexts, 1, None), [None])
            # zip the three iterators so we can iterate over them individually

            self.first = self.last = None
            for prev, box, nxt in zip(prevs, boxes, nexts):
                if not self.first:
                    self.first = prev
                if nxt:
                    self.last = nxt

                node = Pipeline.Node(self.wwdctx, box, prev, nxt)
                print("{} > {} > {}".format(prev, box, nxt))
                self.nodes.append(node)

        print(config)
        print("first: {}, last: {}".format(self.first, self.last))
        print("nodes: {}".format(self.nodes))
