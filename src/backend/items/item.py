import copy
import json
import uuid


class Item:
    def __init__(
        self,
        name: str,
        description: str = "",
        max_quantity: int = 10,
        item_id: str = None
    ):
        self.name = name
        self.description = description
        self.max_quantity = max_quantity
        # Is a unique uuid for the item instance
        self._id: str = item_id or uuid.uuid4().hex

    @property
    def id(self) -> str:
        return self._id

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
        return uuid.uuid5(uuid.NAMESPACE_DNS, serialized).hex

    def clone(self) -> 'Item':
        new_item = copy.deepcopy(self)
        new_item._id = uuid.uuid4().hex  # assign new UUID
        return new_item

    # --- Overrides ---
    def __eq__(self, other: 'Item') -> bool:
        return isinstance(other, Item) and self.id == other.id

    def __repr__(self):
        return f"<Item {self.name} ({self._id})>"
