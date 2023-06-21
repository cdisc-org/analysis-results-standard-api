from typing import List, Optional, Union
from uuid import UUID


from .base_api_model import ApiBaseModel
from .display_section import DisplaySection


class OutputDisplay(ApiBaseModel):
    """
    A tabular representation of the results of one or more analyses.
    """
    id: Union[UUID, None] = None
    name: Optional[str] = None
    version: Optional[int] = None
    order: int
    displayTitle: Optional[str] = None
    displaySections: List[Union[dict, DisplaySection]] = []