from typing import Union, Optional

from .base_api_model import ApiBaseModel
from .data_grouping_factor import DataGroupingFactor


class OrderedGroupingFactor(ApiBaseModel):
    """
    A reference to a defined factor by which subjects or data records are grouped for the analysis, ordered with
    respect to other grouping factors.
    """
    order: int = None
    groupingId: Optional[str] = None
    dataGrouping: Optional[Union[dict, DataGroupingFactor]] = None