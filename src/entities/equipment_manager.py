from typing import List

from items import Equipment

from .item_manager import ItemManager


class EquipmentManager:
    def __init__(self, item_manager: ItemManager):
        self._item_manager = item_manager
        self._equipped = {}

    def __getitem__(self, name: str):
        equipment = self._equipped[name]
        if not equipment:
            raise KeyError(f"Equipment '{name}' not found.")
        return equipment

    def __setitem__(self, name: str, equipment: Equipment):
        item = self._item_manager[name]
        if not item:
            raise KeyError(f"Equipment '{name}' not in items")
        self._equipped[name] = equipment

    def __delitem__(self, name: str):
        if name not in self._equipped:
            raise KeyError(f"Equipment '{name}' not equipped.")
        del self._equipped[name]

    def __contains__(self, name: str) -> bool:
        return name.lower() in self._equipped

    def __iter__(self):
        return iter(self._equipped.keys())

    def __len__(self) -> int:
        return len(self._equipped)

    def equipment_list(self) -> List[Equipment]:
        return list(self._equipped.keys())
