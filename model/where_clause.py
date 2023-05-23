from typing import Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel
from .compound_expression import CompoundExpression
from .condition import Condition


class WhereClause(ApiBaseModel):
    level: Optional[int] = None
    order: Optional[int] = None
    condition: Optional[Condition] = None
    compoundExpression: Optional[CompoundExpression] = None