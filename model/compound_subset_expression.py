from typing import List, Union, Optional
from uuid import UUID

from .ars_enums import LogicalOperator
from .base_api_model import ApiBaseModel
from .where_clause import WhereClause


class CompoundSubsetExpression(ApiBaseModel):
    logicalOperator: Union[str, LogicalOperator] = None
    whereClauses: List[WhereClause] = []
