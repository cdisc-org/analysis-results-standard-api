from model.analysis_categorization import AnalysisCategorization
from model.analysis_category import AnalysisCategory
from model.analysis_group import AnalysisGroup
from model.analysis_method import AnalysisMethod
from model.analysis_output_code_parameter import AnalysisOutputCodeParameter
from model.analysis_output_programming_code import AnalysisOutputProgrammingCode
from model.analysis_programming_code_template import AnalysisProgrammingCodeTemplate
from model.analysis_set import AnalysisSet
from model.analysis import Analysis
from model.code_parameter import CodeParameter
from model.compound_group_expression import CompoundGroupExpression
from model.compound_set_expression import CompoundSetExpression
from model.compound_subset_expression import CompoundSubsetExpression
from model.data_group import DataGroup
from model.data_grouping_factor import DataGroupingFactor
from model.data_subset import DataSubset
from model.display_section import DisplaySection
from model.display_subsection import DisplaySubSection
from model.document_reference import DocumentReference
from model.extensible_terminology_term import ExtensibleTerminologyTerm, AnalysisPurpose, AnalysisReason, SponsorAnalysisReason, SponsorAnalysisPurpose, SponsorOperationRole, OperationRole, SponsorOutputFileType, OutputFileType
from model.output_file import OutputFile
from model.global_display_section import GlobalDisplaySection
from model.group import Group
from model.grouping_factor import GroupingFactor
from model.nested_list import NestedList
from model.operation import Operation
from model.operation_result import OperationResult
from model.ordered_display import OrderedDisplay
from model.ordered_display_subsection import OrderedDisplaySubSection
from model.ordered_subsection import OrderedSubSection
from model.ordered_subsection_ref import OrderedSubSectionRef
from model.ordered_grouping_factor import OrderedGroupingFactor
from model.ordered_list_item import OrderedListItem
from model.output_display import OutputDisplay
from model.output import Output
from model.page_ref import PageRef, PageNameRef, PageNumberRangeRef, PageNumberListRef
from model.referenced_analysis_operation import ReferencedAnalysisOperation
from model.reference_document import ReferenceDocument
from model.referenced_operation_relationship import ReferencedOperationRelationship
from model.reporting_event import ReportingEvent
from model.result_group import ResultGroup
from model.sponsor_term import SponsorTerm
from model.subject_grouping_factor import SubjectGroupingFactor
from model.template_code_parameter import TemplateCodeParameter
from model.terminology_extension import TerminologyExtension
from model.where_clause import WhereClause
from model.where_clause_compound_expression import WhereClauseCompoundExpression
from model.where_clause_condition import WhereClauseCondition

# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
ReportingEvent.update_forward_refs()
NestedList.update_forward_refs()
OrderedListItem.update_forward_refs()
AnalysisCategorization.update_forward_refs()
AnalysisCategory.update_forward_refs()
Analysis.update_forward_refs()
OrderedGroupingFactor.update_forward_refs()
ReferencedAnalysisOperation.update_forward_refs()
OperationResult.update_forward_refs()
ResultGroup.update_forward_refs()
AnalysisMethod.update_forward_refs()
Operation.update_forward_refs()
ReferencedOperationRelationship.update_forward_refs()
AnalysisOutputProgrammingCode.update_forward_refs()
AnalysisProgrammingCodeTemplate.update_forward_refs()
CodeParameter.update_forward_refs()
AnalysisOutputCodeParameter.update_forward_refs()
TemplateCodeParameter.update_forward_refs()
Output.update_forward_refs()
OutputFile.update_forward_refs()
OrderedDisplay.update_forward_refs()
OutputDisplay.update_forward_refs()
DisplaySection.update_forward_refs()
OrderedDisplaySubSection.update_forward_refs()
OrderedSubSection.update_forward_refs()
OrderedSubSectionRef.update_forward_refs()
DisplaySubSection.update_forward_refs()
GlobalDisplaySection.update_forward_refs()
WhereClause.update_forward_refs()
WhereClauseCondition.update_forward_refs()
WhereClauseCompoundExpression.update_forward_refs()
CompoundSetExpression.update_forward_refs()
CompoundGroupExpression.update_forward_refs()
CompoundSubsetExpression.update_forward_refs()
AnalysisSet.update_forward_refs()
GroupingFactor.update_forward_refs()
SubjectGroupingFactor.update_forward_refs()
DataGroupingFactor.update_forward_refs()
Group.update_forward_refs()
AnalysisGroup.update_forward_refs()
DataGroup.update_forward_refs()
DataSubset.update_forward_refs()
ReferenceDocument.update_forward_refs()
DocumentReference.update_forward_refs()
PageRef.update_forward_refs()
PageNumberListRef.update_forward_refs()
PageNumberRangeRef.update_forward_refs()
PageNameRef.update_forward_refs()
TerminologyExtension.update_forward_refs()
SponsorTerm.update_forward_refs()
ExtensibleTerminologyTerm.update_forward_refs()
AnalysisReason.update_forward_refs()
SponsorAnalysisReason.update_forward_refs()
AnalysisPurpose.update_forward_refs()
SponsorAnalysisPurpose.update_forward_refs()
OperationRole.update_forward_refs()
SponsorOperationRole.update_forward_refs()
OutputFileType.update_forward_refs()
SponsorOutputFileType.update_forward_refs()
