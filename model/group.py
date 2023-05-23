from typing import List, Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel
from .compound_group_expression import CompoundGroupExpression


class Group(ApiBaseModel):
    """
    A subdivision of the subject population or analysis dataset record set based on a defined factor.
    """
    id: Union[UUID, str] = None
    label: Optional[str] = None
    compoundExpression: CompoundGroupExpression = None
