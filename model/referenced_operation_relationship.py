from typing import List, Union, Optional
from uuid import UUID
from enum import Enum

from .base_api_model import ApiBaseModel


class OperationRole(Enum):
    NUMERATOR = "NUMERATOR"
    DENOMINATOR = "DENOMINATOR"

class ReferencedOperationRelationship(ApiBaseModel):
    """
    A reference to an statistical operation whose results is used in the calculation of the result for this operation.
    """
    id: Union[UUID, None] = None
    referencedOperationRole: Union[str, "OperationRole"] = None
    operationId: str
    analysisId: Optional[str] = None
    description: Optional[str] = None