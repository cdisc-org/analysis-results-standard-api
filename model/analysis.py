from typing import List, Union
from uuid import UUID

from .base_api_model import ApiBaseModel


class Analysis(ApiBaseModel):
    analysisId: Union[UUID, None] = None
    version: str
    categoryIds: List = []
    analysisSetId: str
    orderedGroupings: List = []
    dataSubsetId: str
    dataset: str
    variable: str
    methodId: str
    referencedAnalysisOperations: List = []
    results: str
