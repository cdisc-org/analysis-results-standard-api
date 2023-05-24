from typing import List, Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel
from .display_sections import DisplaySection


class Display(ApiBaseModel):
    displayid: Union[UUID, None] = None
    name: str = None
    version: Optional[int] = None
    displayTitle: Optional[str] = None
    displaySections: Optional[Union[Union[dict, DisplaySection], List[Union[dict, DisplaySection]]]] = []
