from typing import Union
from uuid import UUID

from .base_api_model import ApiBaseModel


class DisplaySubSection(ApiBaseModel):
    id: Union[UUID, None] = None
    text: str
