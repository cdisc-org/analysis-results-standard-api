from typing import Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel


class ReferencedAnalysisOperation(ApiBaseModel):
    analysisId: Union[UUID, str] = None
    referencedOperationId: Optional[str] = None
