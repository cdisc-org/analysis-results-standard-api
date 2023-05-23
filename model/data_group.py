from typing import Union
from uuid import UUID

from .base_api_model import ApiBaseModel


class DataGroup(ApiBaseModel):
    """
    A subdivision of the analysis dataset records based on a defined factor.
    """
    dataGroupid: Union[UUID, str]
