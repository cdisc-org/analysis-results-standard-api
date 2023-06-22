from typing import Optional, Union
from uuid import UUID

from .base_api_model import ApiBaseModel
from .referenced_operation_relationship import ReferencedOperationRelationship


class Operation(ApiBaseModel):
    """
    A statistical operation that produces a single analysis result value as part of an analysis method.
    """
    id: Union[UUID, None] = None
    name: str
    label: str
    referencedOperationRelationships: Optional[Union[dict, ReferencedOperationRelationship]] = []
    resultPattern: str