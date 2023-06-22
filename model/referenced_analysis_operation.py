from typing import Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel


class ReferencedAnalysisOperation(ApiBaseModel):
    """
    An indication of the analysis that contains results of a referenced operation.
    """
    analysisId: Union[UUID, str] = None
    referencedOperationRelationshipId: Optional[str] = None
