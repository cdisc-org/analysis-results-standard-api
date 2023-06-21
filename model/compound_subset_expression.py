from typing import List, Union, Optional
from uuid import UUID

from .ars_enums import LogicalOperator
from .where_clause import WhereClause
from .where_clause_compound_expression import WhereClauseCompoundExpression


class CompoundSubsetExpression(WhereClauseCompoundExpression):
    logicalOperator: Union[str, LogicalOperator] = None
    whereClauses: List[WhereClause] = []
