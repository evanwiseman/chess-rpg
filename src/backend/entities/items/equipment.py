from .item import Item
from src.backend.foundation import EquipmentSlot


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
