from typing import List, Union, Optional
from uuid import UUID

from .analysis_programming_code_template import AnalysisProgrammingCodeTemplate
from .base_api_model import ApiBaseModel
from .document_reference import DocumentReference
from .operation import Operation


class AnalysisMethod(ApiBaseModel):
    """
    A set of one or more statistical operations.
    """
    id: Union[UUID, str] = None
    name: Optional[str] = None
    operations: List[Union[dict, Operation]] = []
    label: Optional[str] = None
    description: Optional[str] = None
    documentRefs: List[Union[dict, DocumentReference]] = []
    codeTemplate: Optional[Union[dict, AnalysisProgrammingCodeTemplate]] = None
