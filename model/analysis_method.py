from typing import List, Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel
from .operation import Operation


class AnalysisMethod(ApiBaseModel):
    analysisMethodid: Union[UUID, str] = None
    name: str = None
    operations: List[Operation] = []
    label: Optional[str] = None
    description: Optional[str] = None
