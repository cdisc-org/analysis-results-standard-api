from typing import List, Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel
from .display_subsection import DisplaySubSection


class OrderedSubSectionRef(ApiBaseModel):
    """
    A reference to a subsection defined either globally or in another display section, ordered with respect to other
    subsections of the same type.
    """
    order: int = None
    subSection: Optional[Union[dict, DisplaySubSection]] = None
    subSectionId: Optional[str] = None
