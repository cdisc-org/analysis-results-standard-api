from typing import List, Union

from .where_clause_compound_expression import WhereClauseCompoundExpression
from .ars_enums import LogicalOperator

class CompoundSetExpression(WhereClauseCompoundExpression):
    logicalOperator: Union[str, LogicalOperator] = None
    whereClauses: List[str] = []
