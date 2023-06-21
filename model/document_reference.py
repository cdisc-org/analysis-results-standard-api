from typing import List, Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel
from .page_ref import PageRef


class DocumentReference(ApiBaseModel):

    id: Union[UUID, None] = None
    pageRefs: Optional[List[Union[dict, PageRef]]] = []
