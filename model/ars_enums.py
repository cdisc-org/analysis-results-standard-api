from enum import Enum


class LogicalOperator(Enum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"

class DisplaySectionTypeEnum(Enum):
    TITLE = "Title"
    FOOTNOTE = "Footnote"
    ABBREVIATION = "Abbreviation"
    LEGEND = "Legend"

class PageRefTypeEnum(Enum):
    """
    Type of page for page references.
    """
    # References are to page numbers
    PhysicalRef = "PhysicalRef"
    #  References are to named destinations in the referenced document
    NamedDestination = "NamedDestination"

class ExtensibleTerminologyEnum(Enum):
    """
    Extensible ARS enumerations.
    """
    # The rationale for performing this analysis. It indicates when the analysis was planned
    # meaning=NCIT.C117744
    AnalysisReasonEnum = "AnalysisReasonEnum"
    # The purpose of the analysis within the body of evidence (e.g., section in the clinical study report)
    # meaning=NCIT.C117745
    AnalysisPurposeEnum = "AnalysisPurposeEnum"
    OperationRoleEnum = "OperationRoleEnum"
    OutputFileTypeEnum ="OutputFileTypeEnum"

class AnalysisReasonEnum(Enum):
    """
    The rationale for performing this analysis. It indicates when the analysis was planned.
    """
    # The analysis is specified in a protocol
    # meaning=NCIT.C117752
    SIP = "SPECIFIED IN PROTOCOL",
    # The analysis is specified in a statistical analysis plan
    # meaning=NCIT.C117753
    SISAP = "SPECIFIED IN SAP",
    # The analysis was triggered by findings in the data
    # meaning=NCIT.C117750
    DD = "DATA DRIVEN",
    # The analysis has been requested by a regulatory agency
    # meaning=NCIT.C117751
    RBRA = "REQUESTED BY REGULATORY AGENCY",

class AnalysisPurposeEnum(Enum):
    """
    The purpose of the analysis within the body of evidence (e.g., section in the clinical study report).
    """

    # The outcome measure(s) of greatest importance specified in the protocol, usually the one(s) used in the power calculation, to evaluate the primary endpoint(s) associated with the primary study objective(s). (After Clinicaltrials.gov)
    # meaning=NCIT.C98772
    POM = "PRIMARY OUTCOME MEASURE",
    # The outcome measure(s) that is part of a pre-specified analysis plan used to evaluate the secondary endpoint(s) associated with secondary study objective(s) and/or used to evaluate any measure(s) ancillary to the primary or secondary endpoint(s). (After Clinicaltrials.gov)
    # meaning=NCIT.C98781
    SOM = "SECONDARY OUTCOME MEASURE",
    # The outcome measure(s) that is part of a pre-specified analysis plan used to evaluate the exploratory endpoint(s) associated with exploratory study objective(s) and/or any other measures, excluding post-hoc measures, that are a focus of the study. (After clinicaltrials.gov)
    # meaning=NCIT.C98724
    EOM = "EXPLORATORY OUTCOME MEASURE",