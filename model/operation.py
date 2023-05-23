from typing import List, Union
from uuid import UUID

from .base_api_model import ApiBaseModel


class Operation(ApiBaseModel):
    operationId: Union[UUID, None] = None
    name: str
    label: str
    referencedOperationRelationships: List = []
    resultPattern: str