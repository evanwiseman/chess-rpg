from src.backend.entities import Entity
from src.backend.items import (
    Equipment, EquipmentSlot, ItemManager, EquipmentManager
)
from src.backend.stats import StatsManager, ResourceManager
from typing import Optional


class Piece(Entity):
    def __init__(self, name, owner: Optional[object] = None):
        super().__init__(name, owner)

        self.stats = StatsManager()
        self.resources = ResourceManager()
        self.equipped = EquipmentManager()
        self.inventory = ItemManager()

    def equip(self, equipment: Equipment):
        if self.inventory.has_item(equipment):
            self.inventory.remove_item(equipment)
        self.equipped.add_equipment(equipment)

    def equip_slot(self, slot: EquipmentSlot, equipment: Equipment):
        if self.inventory.has_item(equipment):
            self.inventory.remove_item(equipment)
        self.equipped.add_equipment_to_slot(slot, equipment)

    def unequip(self, equipment: Equipment):
        previous = self.equipped.remove_equipment(equipment)
        if previous and self.inventory.has_room():
            self.inventory.add_item(previous)
        else:
            raise RuntimeError("Cannot unequip: inventory full")

    def unequip_slot(self, slot: EquipmentSlot):
        previous = self.equipped.remove_equipment_from_slot(slot)
        if previous and self.inventory.has_room():
            self.inventory.add_item(previous)
        else:
            raise RuntimeError("Cannot unequip: inventory full")
