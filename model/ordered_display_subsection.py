from typing import List, Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel
from .display_subsection import DisplaySubSection


class OrderedDisplaySubSection(ApiBaseModel):
    order: int = None
    subSection: Optional[Union[dict, DisplaySubSection]] = None
    subSectionId: Optional[str] = None
