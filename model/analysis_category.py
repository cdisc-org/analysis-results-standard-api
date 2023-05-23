from typing import List, Union
from uuid import UUID

from .base_api_model import ApiBaseModel


class AnalysisCategory(ApiBaseModel):
    analysisCategoryId: Union[UUID, None] = None
    label: str = ""
    subCategorizations: List = []
