import copy

from typing import List

from .items import Equipment
from .item_manager import ItemManager


class EquipmentManager:
    def __init__(self, item_manager: ItemManager):
        self._equipped: dict[str, Equipment] = {}
        self._item_manager = item_manager

    def get_equip(self, name: str) -> Equipment:
        """
        Return Equipment if equipped. Raises KeyError if not found.
        """
        key = name.lower()
        equipment = self._equipped.get(key)
        if not equipment:
            raise KeyError(f"Equipment '{name}' not equipped.")
        return equipment

    def equip(self, name: str, quantity: int = 1) -> bool:
        """
        Move an equipment item from the ItemManager into equipped.
        Returns True if successful, False otherwise.
        """
        key = name.lower()
        try:
            equipment = self._item_manager.remove_item(name, quantity)
            if not isinstance(equipment, Equipment):
                raise TypeError(f"Item '{name}' is not equippable.")
            self._equipped[key] = equipment
        except (KeyError, ValueError, TypeError):
            return False
        return True

    def unequip(self, name: str, quantity: int = 1) -> Equipment:
        """
        Unequip an item and return it to the ItemManager.
        Raises KeyError if not equipped.
        """
        key = name.lower()
        if key not in self._equipped:
            raise KeyError(f"Equipment '{name}' not equipped.")

        equipment = self._equipped[key]

        if quantity < equipment.quantity:
            # Split stack: put part back into inventory
            equipment.quantity -= quantity
            new_equipment = copy.deepcopy(equipment)
            new_equipment.quantity = quantity
            self._item_manager.add_item(name, new_equipment)
            return new_equipment

        self._item_manager.add_item(name, equipment)
        del self._equipped[key]
        return equipment

    def get_equipped(self) -> List[str]:
        return list(self._equipped.keys())
