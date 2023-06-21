from typing import Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel


class ResultGroup(ApiBaseModel):
    """
    For the specified grouping factor, an indication of the specific group of subjects or data records associated with
    the analysis result.
    """
    groupingId: Union[UUID, str]
    groupId: Optional[str] = None
    groupValue: Optional[str] = None