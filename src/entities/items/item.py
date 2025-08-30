from enum import Enum

from src.entities import Entity


class ItemType(Enum):
    CONSUMABLE = "consumable"


class Item(Entity):
    def __init__(self, name):
        super().__init__(name)
