from typing import List, Union

from .ars_enums import LogicalOperator
from .where_clause import WhereClauseCompoundExpression


class CompoundGroupExpression(WhereClauseCompoundExpression):
    logicalOperator: Union[str, LogicalOperator] = None
    whereClauses: List[str]= []
