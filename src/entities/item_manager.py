from typing import List

from .items import Item


class ItemManager:
    def __init__(self):
        self._items = {}

    def __getitem__(self, name: str) -> Item:
        item = self._items.get(name.lower())
        if not item:
            raise KeyError(f"Item '{item}' not found.")
        return item

    def __setitem__(self, name: str, item: Item):
        self._items[name.lower()] = item

    def __contains__(self, name: str) -> bool:
        return name.lower() in self._items

    def __iter__(self):
        return iter(self._items.keys())

    def __len__(self) -> int:
        return len(self._items)

    def item_list(self) -> List[Item]:
        return list(self._items.keys())
