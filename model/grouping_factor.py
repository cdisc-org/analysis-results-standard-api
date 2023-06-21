from typing import List, Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel
from .group import Group


class GroupingFactor(ApiBaseModel):
    """
    A factor used to subdivide either the subject population or data records in an analysis dataset for analysis.
    """
    id: Union[UUID, str] = None
    dataDriven: Optional[bool] = None
    label: Optional[str] = None
    groupingVariable: Optional[str] = None
    groups: List[Union[dict, Group]] = []
