# Copyright 2016 Cisco Systems, Inc.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from distutils.version import StrictVersion

from neutron.tests.common import base
from neutron.tests.unit import testlib_api
from neutron import version

# Some constants and verifier functions have been deprecated but are still
# used by earlier releases of neutron. In order to maintain
# backwards-compatibility with stable/mitaka this will act as a translator
# that passes constants and functions according to version number.

if StrictVersion(str(version.version_info)) >= StrictVersion('9.0.0'):
    from neutron.conf import common as base_config
    from neutron_lib.api import validators
    from neutron_lib import constants
    ATTR_NOT_SPECIFIED = constants.ATTR_NOT_SPECIFIED
    is_attr_set = validators.is_attr_set
    IS_PRE_NEWTON = False

    class MySQLTestCase(testlib_api.MySQLTestCaseMixin,
            testlib_api.SqlTestCaseLight):
        pass
else:
    from neutron.api.v2 import attributes
    from neutron.common import config as base_config
    ATTR_NOT_SPECIFIED = attributes.ATTR_NOT_SPECIFIED
    is_attr_set = attributes.is_attr_set
    IS_PRE_NEWTON = True

    class MySQLTestCase(base.MySQLTestCase):
        pass
core_opts = base_config.core_opts
