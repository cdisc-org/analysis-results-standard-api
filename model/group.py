from typing import List, Union, Optional
from uuid import UUID

from .compound_group_expression import CompoundGroupExpression
from .where_clause import WhereClause


class Group(WhereClause):
    """
    A subdivision of the subject population or analysis dataset record set based on a defined factor.
    """
    id: Union[UUID, str] = None
    label: Optional[str] = None
    compoundExpression: CompoundGroupExpression = None
