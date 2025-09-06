import json
import uuid
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
    ):
        # Equipment is not stackable
        super().__init__(name, description, 1)
        self._slot = slot

    @property
    def slot(self) -> EquipmentSlot:
        return self._slot

    def type_id(self):
        content = {
            "name": self.name,
            "max_quantity": self.max_quantity,
            "slot": self.slot.value
        }
        serialized = json.dumps(content, sort_keys=True)
        return uuid.uuid5(uuid.NAMESPACE_DNS, serialized).hex

    def __eq__(self, other: 'Equipment'):
        return (
            isinstance(other, Equipment)
            and super().__eq__(other)
            and self.slot == other.slot
        )
