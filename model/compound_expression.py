from typing import List, Union

from .ars_enums import LogicalOperator
from .base_api_model import ApiBaseModel
from .where_clause import WhereClause


class CompoundExpression(ApiBaseModel):
    logicalOperator: Union[str, LogicalOperator] = None
    whereClauses: List[Union[dict, WhereClause]] = []
