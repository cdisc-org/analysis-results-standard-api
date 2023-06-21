from typing import Union
from uuid import UUID

from .group import Group


class DataGroup(Group):
    """
    A subdivision of the analysis dataset records based on a defined factor.
    """
    id: Union[UUID, str]
