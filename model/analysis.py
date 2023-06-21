from typing import List, Union, Optional
from uuid import UUID

from analysis_output_programming_code import AnalysisOutputProgrammingCode
from .base_api_model import ApiBaseModel
from .document_reference import DocumentReference
from .extensible_terminology_term import ExtensibleTerminologyTerm
from .operation_result import OperationResult
from .ordered_grouping_factor import OrderedGroupingFactor
from .referenced_analysis_operation import ReferencedAnalysisOperation


class Analysis(ApiBaseModel):
    """
    An analysis that is designed to meet a requirement of the reporting event. Each analysis is defined as a set of
    specifications, including:
    * The analysis variable that is the subject of the analysis.
    * The analysis method (set of statistical operations) that is performed for the analysis variable.
    * The analysis set (subject population) for which the analysis is performed.
    * The subset of data records on which the analysis is performed (optional).
    * One or more factors by which either subjects or data records are grouped for analysis (optional).
    """
    id: Union[UUID, None] = None
    name: Optional[str] = None
    description: Optional[str] = None
    version: Optional[int] = None
    categoryIds: List[str] = []
    analysisSetId: Optional[str] = None
    orderedGroupings: List[Union[dict, OrderedGroupingFactor]] = []
    dataSubsetId: Optional[str]
    dataset: Optional[str] = None
    variable: Optional[str] = None
    methodId: Optional[str] = None
    referencedAnalysisOperations: Optional[List[Union[dict, ReferencedAnalysisOperation]]] = []
    results: str
    documentRefs: List[Union[dict, DocumentReference]] = []
    results: List[Union[dict, OperationResult]] = []
    reason: Optional[Union[dict, ExtensibleTerminologyTerm]] = None
    purpose: Optional[Union[dict, ExtensibleTerminologyTerm]] = None
    programmingCode: Optional[Union[dict, AnalysisOutputProgrammingCode]] = None
