from typing import List, Union, Optional
from uuid import UUID
from enum import Enum

from .base_api_model import ApiBaseModel


class FileType(Enum):
    PDF = "pdf"
    RTF = "rtf"
    TXT = "txt"


class File(ApiBaseModel):
    name: str = None
    fileType: Optional[Union[str, "FileType"]] = None
    location: Optional[str] = None
    style: Optional[str] = None