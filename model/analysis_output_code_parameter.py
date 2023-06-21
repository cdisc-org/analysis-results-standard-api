from typing import List, Union

from .base_api_model import ApiBaseModel


class AnalysisOutputCodeParameter(ApiBaseModel):
    """
    A parameter whose value is used in programming code for a specific analysis or output.
    """
    name: str = None
    value: Union[str, List[str]] = None

