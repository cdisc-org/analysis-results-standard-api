from typing import Optional, Union

from .ars_enums import AnalysisReasonEnum, AnalysisPurposeEnum
from .base_api_model import ApiBaseModel


class ExtensibleTerminologyTerm(ApiBaseModel):
    """
    A sponsor-defined term that is included in an extensible set of controlled terminology.
    """
    controlledTerm: Optional[str] = None
    sponsorTermId: Optional[str] = None

class AnalysisReason(ExtensibleTerminologyTerm):

    controlledTerm: Union[str, AnalysisReasonEnum] = None
    sponsorTermId: Optional[str] = None

class SponsorAnalysisReason(ExtensibleTerminologyTerm):

    controlledTerm: Optional[str] = None
    sponsorTermId: Optional[str] = None

class AnalysisPurpose(ExtensibleTerminologyTerm):

    controlledTerm: Union[str, AnalysisPurposeEnum] = None
    sponsorTermId: Optional[str] = None