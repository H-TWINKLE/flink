################################################################################
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
# limitations under the License.
################################################################################
from typing import Union

from py4j.java_gateway import JavaObject

from pyflink.datastream.functions import JavaFunctionWrapper


class InputFormat(JavaFunctionWrapper):
    """
    The Python wrapper of Java InputFormat interface, which is the base interface for data sources
    that produce records.
    """

    def __init__(self, source: Union[str, JavaObject]):
        super().__init__(source)
