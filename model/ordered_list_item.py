from typing import Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel
from .nested_list import NestedList


class OrderedListItem(ApiBaseModel):
    name: str = None
    level: int = None
    order: int = None
    sublist: Optional[Union[dict, NestedList]] = None
    analysisId: Optional[str] = None
    outputId: Optional[str] = None
