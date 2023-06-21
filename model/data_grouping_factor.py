from typing import List, Union
from uuid import UUID

from .data_group import DataGroup
from .grouping_factor import GroupingFactor


class DataGroupingFactor(GroupingFactor):
    id: Union[UUID, str] = None
    dataDriven: bool
    groups: List[Union[dict, DataGroup]] = []
