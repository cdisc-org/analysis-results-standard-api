from typing import Union, Optional
from uuid import UUID

from .base_api_model import ApiBaseModel


class SponsorTerm(ApiBaseModel):
    """
    A sponsor-defined term that is included in an extensible set of controlled terminology.
    """
    id: Union[UUID, None] = None
    submissionValue: str = None
    description: Optional[str] = None