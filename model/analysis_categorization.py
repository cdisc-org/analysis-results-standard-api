from typing import List, Union
from uuid import UUID

from .base_api_model import ApiBaseModel


class AnalysisCategorization(ApiBaseModel):
    """
    A set of related implementer-defined categories that can be used to categorize analyses or outputs.
    """
    id: Union[UUID, None] = None
    label: str = ""
    categories: List = []
