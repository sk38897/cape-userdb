# Copyright 2018 BLEMUNDSBURY AI LIMITED
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

from typing import Union
from peewee import CharField

from cape_userdb.base import BaseDB


class HangoutsSpace(BaseDB):
    # Inherited fields are:
    # modified: Union[DateTimeField, datetime.datetime] = DateTimeField(index=True, default=utc_now)
    # id: int
    user_id: Union[CharField, str] = CharField(index=True)
    space_id: Union[CharField, str] = CharField(index=True, unique=True)
