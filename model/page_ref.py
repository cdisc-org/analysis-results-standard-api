from typing import List, Union, Optional

from .ars_enums import PageRefTypeEnum
from .base_api_model import ApiBaseModel


class PageRef(ApiBaseModel):
    refType: Union[str, PageRefTypeEnum] = None
    label: Optional[str] = None
    pageNames: Optional[Union[str, List[str]]] = []
    pageNumbers: Optional[Union[int, List[int]]] = []
    firstPage: Optional[int] = None
    lastPage: Optional[int] = None

class PageNumberListRef(PageRef):
    """
    One or more individual pages in the reference document, referenced by page number.
    """

    refType: Union[str, PageRefTypeEnum] = None
    pageNumbers: Union[int, List[int]] = None
    pageNames: Optional[Union[str, List[str]]] = []
    firstPage: Optional[int] = None
    lastPage: Optional[int] = None

class PageNumberRangeRef(PageRef):
    """
    A range of pages in the reference document, indicated by the first and last page number in the range.
    """

    refType: Union[str, PageRefTypeEnum] = None
    firstPage: int = None
    lastPage: int = None
    pageNumbers: Optional[Union[int, List[int]]] = []
    pageNames: Optional[Union[str, List[str]]] = []

class PageNameRef(PageRef):
    """
    One or more pages in the reference document, referenced by named destination.
    """
    refType: Union[str, PageRefTypeEnum] = None
    pageNames: Union[str, List[str]] = None
    pageNumbers: Optional[Union[int, List[int]]] = []
    firstPage: Optional[int] = None
    lastPage: Optional[int] = None