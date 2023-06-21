from typing import Optional, TYPE_CHECKING


from .base_api_model import ApiBaseModel
if TYPE_CHECKING:
    from .where_clause_compound_expression import WhereClauseCompoundExpression
from .where_clause_condition import WhereClauseCondition


class WhereClause(ApiBaseModel):
    level: Optional[int] = None
    order: Optional[int] = None
    condition: Optional[WhereClauseCondition] = None
    compoundExpression: Optional[WhereClauseCompoundExpression] = None