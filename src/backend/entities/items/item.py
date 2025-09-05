import hashlib
import json
from src.backend.entities.base import Interactable


class Item(Interactable):
    def __init__(
        self, name: str,
        description: str = "",
        max_quantity: int = 10
    ):
        super().__init__(name)
        self.description = description
        self.max_quantity = max_quantity

    def item_eq(self, other: 'Item'):
        """
        Compares all attributes
        """
        return (
            self.name == other.name
            and self.max_quantity == other.max_quantity
        )

    @property
    def type_id(self) -> str:
        """
        Returns a stable hash of the item's content (ignoring unique ID).
        Used for item stacking.
        """
        # Gather only the fields that define the item's logic
        content = {
            "name": self.name,
            "max_quantity": self.max_quantity
        }
        serialized = json.dumps(content, sort_keys=True)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()
