from typing import Tuple, List

from src.entities import Entity
from src.stats import Stats, Stat
from src.systems import ItemManager, EquipmentManager


class Piece(Entity):
    def __init__(self, name: str):
        super().__init__(name)
        self.directions: List[Tuple[int, int]] = []

        self.stats = Stats()
        self.stats["value"] = Stat("Value", 0)
        self.stats["max_health"] = Stat("Max Health", 0)
        self.stats["damage"] = Stat("Damage", 0)
        self.stats["range"] = Stat("Range", 0)

        self._item_manager = ItemManager()
        self._equipment_manager = EquipmentManager()

    def __eq__(self, other: 'Piece'):
        return (
            self.name == other.name
            and self.stats == other.stats
        )
