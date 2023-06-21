from typing import List, Union, Optional
from uuid import UUID

from .analysis_output_programming_code import AnalysisOutputProgrammingCode
from .base_api_model import ApiBaseModel
from .document_reference import DocumentReference
from .ordered_display import OrderedDisplay
from .output_file import OutputFile
from .output_display import OutputDisplay


class Output(ApiBaseModel):
    """
    A report of results and their evaluation based on planned analyses performed during the course of a trial.
    """
    id: Union[UUID, None] = None
    name: Optional[str] = None
    version: Optional[int] = None
    fileSpecifications: Optional[List[Union[dict, OutputFile]]] = []
    outputDisplays: Optional[Union[Union[dict, OutputDisplay], List[Union[dict, OutputDisplay]]]] = []
    categoryIds: Optional[Union[str, List[str]]] = []
    displays: Optional[List[Union[dict, OrderedDisplay]]] = []
    documentRefs: Optional[List[Union[dict, DocumentReference]]] = []
    programmingCode: Optional[Union[dict, AnalysisOutputProgrammingCode]] = None