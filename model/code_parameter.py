from typing import List, Union, Optional
from enum import Enum

from .base_api_model import ApiBaseModel


class CodeParameter(ApiBaseModel):
    """
    A replacement parameter whose value is substituted in template programming code to create statements required for
    a specific analysis.
    """
    name: Optional[str] = None
    description: Optional[str] = None
    