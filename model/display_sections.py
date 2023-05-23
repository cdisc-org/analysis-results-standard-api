from typing import List, Union, Optional
from uuid import UUID
from enum import Enum

from .base_api_model import ApiBaseModel
from .display_subsection import DisplaySubSection

class SectionType(Enum):
    TITLE = "Title"
    FOOTNOTE = "Footnote"
    ABBREVIATION = "Abbreviation"
    LEGEND = "Legend"

class DisplaySection(ApiBaseModel):
    sectionType: Optional[Union[str, SectionType]] = None
    subSections: List[DisplaySubSection] = []
