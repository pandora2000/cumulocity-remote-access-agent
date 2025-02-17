#  Copyright (c) 2021 Software AG, Darmstadt, Germany and/or its licensors
#
#  SPDX-License-Identifier: Apache-2.0
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from setuptools import setup

setup(name='c8y-device-proxy',
      version='1.0.3',
      description='Cumulocity Device Proxy',
      author='Stefan Witschel',
      license='Apache v2',
      packages=['c8ydp'],
      install_requires = [
        'certifi>=2021.5.30',
        'websocket_client>=1.1.0'
      ],
      zip_safe=False)
