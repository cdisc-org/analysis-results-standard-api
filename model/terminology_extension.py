from typing import List, Union, Optional
from uuid import UUID

from .ars_enums import ExtensibleTerminologyEnum
from .base_api_model import ApiBaseModel
from .sponsor_term import SponsorTerm


class TerminologyExtension(ApiBaseModel):
    """
    A sponsor-defined term that is included in an extensible set of controlled terminology.
    """
    id: Union[UUID, None] = None
    sponsorTerms: List[Union[dict, SponsorTerm]] = []
    enumeration: Optional[Union[str, ExtensibleTerminologyEnum]] = None