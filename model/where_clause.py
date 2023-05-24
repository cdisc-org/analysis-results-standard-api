from typing import Optional, TYPE_CHECKING


from .base_api_model import ApiBaseModel
if TYPE_CHECKING:
    from .compound_expression import CompoundExpression
from .condition import Condition


class WhereClause(ApiBaseModel):
    level: Optional[int] = None
    order: Optional[int] = None
    condition: Optional[Condition] = None
    compoundExpression: Optional["CompoundExpression"] = None