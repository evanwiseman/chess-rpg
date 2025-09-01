from src.entities import Entity
from src.stats import Stats
from src.systems import ItemManager, EquipmentManager


class Piece(Entity):
    def __init__(self, name: str):
        super().__init__(name)
        self.stats = Stats()
        self.stats.add("value", 0)
        self.stats.add("max_health", 0)
        self.stats.add("damage", 0)
        self.stats.add("range", 0)

        self._item_manager = ItemManager()
        self._equipment_manager = EquipmentManager()

    def __eq__(self, other: 'Piece'):
        return (
            self.name == other.name
            and self.stats == other.stats
        )
