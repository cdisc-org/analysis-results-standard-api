from typing import List, Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel
from .result_group import ResultGroup


class OperationResult(ApiBaseModel):
    """
    The result of an analysis method operation performed on a subdivision of subjects or data records.
    """
    operationId: str
    resultGroups: List[ResultGroup] = []
    rawValue: Optional[str] = None
    formattedValue: Optional[str] = None