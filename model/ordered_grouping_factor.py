from typing import Union, Optional

from .base_api_model import ApiBaseModel
from .data_grouping_factor import DataGroupingFactor


class OrderedGroupingFactor(ApiBaseModel):
    order: int = None
    groupingId: Optional[str] = None
    dataGrouping: Optional[Union[dict, DataGroupingFactor]] = None