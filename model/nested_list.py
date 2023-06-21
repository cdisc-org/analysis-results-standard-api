from typing import List, Union, TYPE_CHECKING

from .base_api_model import ApiBaseModel
if TYPE_CHECKING:
    from .ordered_list_item import OrderedListItem


class NestedList(ApiBaseModel):
    """
    A list of items (analyses or outputs) that may be organized within sub-lists.
    """
    listItems: List[Union[dict, "OrderedListItem"]] = []

