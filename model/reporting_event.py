from typing import List, Union, Optional
from uuid import UUID

from .analysis import Analysis
from .analysis_categorization import AnalysisCategorization
from .analysis_method import AnalysisMethod
from .analysis_set import AnalysisSet
from .base_api_model import ApiBaseModel
from .data_grouping_factor import DataGroupingFactor
from .data_subset import DataSubset
from .display_section import DisplaySection
from .nested_list import NestedList
from .output import Output
from .reference_document import ReferenceDocument
from .subject_grouping_factor import SubjectGroupingFactor
from .terminology_extension import TerminologyExtension


class ReportingEvent(ApiBaseModel):
    """
    A set of analyses and outputs created to meet a specific reporting requirement, such as a CSR or interim analysis.
    """
    id: Union[UUID, None] = None
    name: str = None
    version: Optional[int] = None
    listOfPlannedOutputs: Optional[Union[dict, NestedList]] = None
    analysisSets: List[Union[dict, AnalysisSet]] = []
    analysisGroupings: List[Union[dict, SubjectGroupingFactor]] = []
    dataSubsets: List[Union[dict, DataSubset]] = []
    dataGroupings:  List[Union[dict, DataGroupingFactor]] = []
    globalDisplaySections: List[Union[dict, DisplaySection]] = []
    analysisCategorizations: List[Union[dict, AnalysisCategorization]] = []
    analyses: List[Union[dict, Analysis]] = []
    methods: List[Union[dict, AnalysisMethod]] = []
    outputs: List[Union[dict, Output]] = []
    referenceDocuments: List[Union[dict, ReferenceDocument]] = []
    terminologyExtensions: List[Union[dict, TerminologyExtension]] = []

