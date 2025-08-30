import copy

from typing import Dict, List

from .entity import Entity
from .items import Item


class ItemManager(Entity):
    def __init__(self):
        self._items: Dict[str, Item] = {}

    def get_item(self, name: str) -> Item:
        key = name.lower()
        item = self._items.get(key)
        if not item:
            raise KeyError(f"Item '{name}' not found.")
        return item

    def add_item(self, name: str, item: Item):
        key = name.lower()
        if name not in self._items:
            self._items[key] = item
        else:
            self._items[key].quantity += item.quantity

    def remove_item(self, name: str, quantity: int | None = None) -> Item:
        key = name.lower()
        item = self._items.get(key)
        if not item:
            raise KeyError(f"Item '{name}' not found.")

        if quantity:
            if item.quantity > quantity:
                item.quantity -= quantity
                new_item = copy.deepcopy(item)
                new_item.quantity = quantity
                return new_item
            elif item.quantity < quantity:
                raise ValueError(
                    f"Item '{name}' cannot remove {quantity}/{item.quantity}."
                )
            # equal case -> fall through below

        # either no quantity given OR equal quantity → remove all
        del self._items[key]
        return item

    def get_item_name_list(self) -> List[str]:
        return list[self._items.keys()]

    def get_item_list(self) -> List[Item]:
        return list[self._items.values()]
