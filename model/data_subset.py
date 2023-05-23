from typing import Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel
from .compound_subset_expression import CompoundSubsetExpression


class DataSubset(ApiBaseModel):
    id: Union[UUID, str] = None
    label: Optional[str] = None
    compoundExpression: Optional[Union[dict, CompoundSubsetExpression]] = None

