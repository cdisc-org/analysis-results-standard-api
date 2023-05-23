from typing import List, Union

from .base_api_model import ApiBaseModel
from .ordered_list_item import OrderedListItem


class NestedList(ApiBaseModel):
    listItems: List[Union[dict, "OrderedListItem"]] = []

