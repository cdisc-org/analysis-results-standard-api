from typing import List, Union
from uuid import UUID

from .base_api_model import ApiBaseModel


class AnalysisCategorization(ApiBaseModel):
    analysisCategorizationId: Union[UUID, None] = None
    label: str = ""
    categories: List = []
