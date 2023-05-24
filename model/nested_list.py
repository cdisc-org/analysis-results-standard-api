from typing import List, Union, TYPE_CHECKING

from .base_api_model import ApiBaseModel
if TYPE_CHECKING:
    from .ordered_list_item import OrderedListItem


class NestedList(ApiBaseModel):
    listItems: List[Union[dict, "OrderedListItem"]] = []

