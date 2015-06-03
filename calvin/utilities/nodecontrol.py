# -*- coding: utf-8 -*-

# Copyright (c) 2015 Ericsson AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from calvin.runtime.north import calvin_node
from calvin.utilities.utils import get_node_id, get_node


def node_control(control_uri):
    class NodeControl(object):

        def __init__(self, control_uri):
            super(NodeControl, self).__init__()
            self._id = None
            self._uri = None
            self.control_uri = control_uri

        @property
        def id(self):
            if self._id is None:
                self._id = get_node_id(self)
            return self._id

        @property
        def uri(self):
            if self._uri is None:
                self._uri = get_node(self, self.id)["uri"]
            return self._uri

    return NodeControl(control_uri)


def dispatch_node(uri, control_uri, trace=False, attributes=None):
    calvin_node.start_node(uri, control_uri, trace, attributes)
    return node_control(control_uri)