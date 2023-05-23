from typing import List, Union
from uuid import UUID

from .base_api_model import ApiBaseModel
from .operation import Operation 


class Method(ApiBaseModel):
  methodId: Union[UUID, None] = None
  label: str
  description: str
  operations: List[Operation] = []