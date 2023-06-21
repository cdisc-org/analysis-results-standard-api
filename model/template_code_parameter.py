from typing import List, Optional, Union

from .base_api_model import ApiBaseModel


class TemplateCodeParameter(ApiBaseModel):
    """
    A replacement parameter whose value is substituted in template programming code to create statements required for
    a specific analysis.
    """
    name: Optional[str] = None
    valueSource: Optional[str] = None
    value: Optional[Union[str, List[str]]] = []

