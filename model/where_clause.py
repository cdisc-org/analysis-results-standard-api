from typing import List, Optional, Union

from model.ars_enums import LogicalOperator
from model.base_api_model import ApiBaseModel


from .base_api_model import ApiBaseModel
from .where_clause_condition import WhereClauseCondition


class WhereClauseCompoundExpression(ApiBaseModel):
    logicalOperator: Union[str, LogicalOperator] = None
    whereClauses: List[Union[dict, "WhereClause"]] = []


class WhereClause(ApiBaseModel):
    level: Optional[int] = None
    order: Optional[int] = None
    condition: Optional[WhereClauseCondition] = None
    compoundExpression: Optional["WhereClauseCompoundExpression"] = None
