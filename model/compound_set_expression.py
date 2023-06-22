from typing import List, Union

from .where_clause import WhereClauseCompoundExpression
from .ars_enums import LogicalOperator

class CompoundSetExpression(WhereClauseCompoundExpression):
    logicalOperator: Union[str, LogicalOperator] = None
    whereClauses: List[str] = []
