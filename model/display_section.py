from typing import List, Union, Optional

from .ars_enums import DisplaySectionTypeEnum
from .base_api_model import ApiBaseModel
from .ordered_display_subsection import OrderedDisplaySubSection


class DisplaySection(ApiBaseModel):
    """
    A part of a tabular display containing one or more pieces of informational text.
    """
    sectionType: Optional[Union[str, DisplaySectionTypeEnum]] = None
    orderedSubSections: Optional[List[Union[dict, OrderedDisplaySubSection]]] = []

