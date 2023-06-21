from typing import Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel


class ReferenceDocument(ApiBaseModel):

    id: Union[UUID, None] = None
    name: str = None
    location: Optional[str] = None
