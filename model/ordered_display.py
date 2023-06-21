from typing import List, Optional, Union
from uuid import UUID


from .base_api_model import ApiBaseModel
from .output_display import OutputDisplay


class OrderedDisplay(ApiBaseModel):
    """
    A display ordered with respect to other displays in an analysis output.
    """
    order: int = None
    display: Optional[Union[dict, OutputDisplay]] = None