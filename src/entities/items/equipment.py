from enum import Enum

from .item import Item


class EquipmentSlot(Enum):
    HELMET = "helmet"
    ARMOR = "armor"
    GLOVES = "gloves"
    LEGS = "legs"
    BOOTS = "boots"
    RING = "ring"
    NECKLACE = "necklace"


class Equipment(Item):
    """
    Container to store equipment(item).
    Not stackable quantity.
    """
    def __init__(
        self,
        name: str,
        slot: EquipmentSlot,
        description: str = "",
        quantity: int = 1
    ):
        super().__init__(name, description, quantity)
        self.slot = slot

    def __eq__(self, other: 'Equipment'):
        return (
            super().__eq__(other)
            and self.slot == other.slot
        )
