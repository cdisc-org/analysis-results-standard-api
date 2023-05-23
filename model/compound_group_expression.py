from typing import List, Union

from .ars_enums import LogicalOperator
from .base_api_model import ApiBaseModel


class CompoundGroupExpression(ApiBaseModel):
    logicalOperator: Union[str, LogicalOperator] = None
    whereClauses: List[str]= []
