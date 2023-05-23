from typing import Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel


class ResultGroup(ApiBaseModel):
    groupingId: Union[UUID, str]
    groupId: Optional[str] = None
    groupValue: Optional[str] = None