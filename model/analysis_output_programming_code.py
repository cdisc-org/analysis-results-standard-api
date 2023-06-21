from typing import List, Optional, Union
from uuid import UUID

from .analysis_output_code_parameter import AnalysisOutputCodeParameter
from .base_api_model import ApiBaseModel
from .document_reference import DocumentReference


class AnalysisOutputProgrammingCode(ApiBaseModel):
    """
    Programming statements and/or a reference to the program used to perform a specific analysis or create a specific
    output.
    """
    context: Optional[str] = None
    code: Optional[str] = None
    documentRef: Optional[Union[dict, DocumentReference]] = None
    parameters: Optional[List[Union[dict, AnalysisOutputCodeParameter]]] = []

