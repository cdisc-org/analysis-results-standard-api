from typing import Union, Optional
from enum import Enum

from .base_api_model import ApiBaseModel
from .extensible_terminology_term import ExtensibleTerminologyTerm


class FileType(Enum):
    PDF = "pdf"
    RTF = "rtf"
    TXT = "txt"


class OutputFile(ApiBaseModel):
    name: str = None
    fileType: Optional[Union[str, ExtensibleTerminologyTerm]] = None
    location: Optional[str] = None
    style: Optional[str] = None
