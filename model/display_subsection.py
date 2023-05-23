from typing import List, Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel


class DisplaySubSection(ApiBaseModel):
    displaySectionId: Union[UUID, None] = None
    order: int
    text: str
