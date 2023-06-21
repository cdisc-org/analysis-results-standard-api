from typing import List, Union
from uuid import UUID

from .base_api_model import ApiBaseModel


class AnalysisCategory(ApiBaseModel):
    """
    An implementer-defined category of analyses/outputs, which may include one or more sub-categorization.
    """
    id: Union[UUID, None] = None
    label: str = ""
    subCategorizations: List = []
