from .base_api_model import ApiBaseModel
from .display import Display


class OutputDisplay(ApiBaseModel):
    # outputDisplayId: Union[UUID, None] = None
    order: int
    display: Display
