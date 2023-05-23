from typing import List, Union
from uuid import UUID

from .base_api_model import ApiBaseModel
from .data_group import DataGroup


class DataGroupingFactor(ApiBaseModel):
    id: Union[UUID, str] = None
    dataDriven: bool
    groups: List[Union[dict, DataGroup]] = []
