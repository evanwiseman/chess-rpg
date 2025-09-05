import copy
from collections import defaultdict
from typing import Dict, List
from .item import Item
from .item_stack import ItemStack


class ItemManager:
    def __init__(self):
        # Track every item instance by unique ID
        self._id_to_item: Dict[int, Item] = {}

        # Name -> list of item IDs (for UI/lookup)
        self._name_to_ids: Dict[str, List[int]] = defaultdict(list)

        # TypeID -> list of ItemStacks
        self._type_id_to_stack: Dict[str, ItemStack] = {}

    def _get_type_id(self, item: Item) -> str:
        return item.type_id

    def add_item(self, item: Item, quantity: int = 1):
        """Add quantity of an item to inventory, respecting max_quantity."""
        if quantity <= 0:
            raise ValueError("Cannot add negative or 0 items")

        type_id = self._get_type_id(item)
        if type_id not in self._type_id_to_stack:
            item_stack = ItemStack([item])
            if not item_stack.has_space(quantity):
                raise ValueError(
                    f"Cannot add more than max {item.max_quantity} {item.name}"
                )
        else:
            item_stack = self._type_id_to_stack[type_id]
            if not item_stack.has_space(quantity):
                raise ValueError(
                    f"Cannot add more than max {item.max_quantity} {item.name}"
                )
            item_stack.push_item(item)

        self._id_to_item[item.id] = item
        self._name_to_ids[item.name].append(item.id)
        for _ in range(quantity - 1):
            new_item = copy.deepcopy(item)
            item_stack.push_item(new_item)
            self._id_to_item[new_item.id] = new_item
            self._name_to_ids[new_item.name].append(item.id)

    def remove_item(self, item: Item, quantity: int = 1) -> List[Item]:
        """Remove quantity of items by name from inventory."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        available_ids = self._name_to_ids.get(item.name, [])
        if len(available_ids) < quantity:
            raise ValueError(
                f"Cannot remove {quantity} {item.name}(s)"
            )

        removed_items: List[Item] = []
        for _ in range(quantity):
            item_id = available_ids.pop()
            item_to_remove = self._id_to_item.pop(item_id)
            removed_items.append(item_to_remove)

            # Remove from stack
            type_id = item_to_remove.type_id
            stack = self._type_id_to_stack.get(type_id)
            if stack:
                stack._items.remove(item_to_remove)
                if stack.is_empty():
                    del self._type_id_to_stack[type_id]
        return removed_items

    def get_quantity(self, item: Item) -> int:
        """Return total quantity of an item by name."""
        item_stack = self._type_id_to_stack.get(item.type_id)
        if not item_stack:
            return 0
        return item_stack.quantity

    def has_item(self, item_name: str, quantity: int = 1) -> bool:
        return self.get_quantity(item_name) >= quantity

    def get_items_by_name(self, item_name: str) -> List[Item]:
        ids = self._name_to_ids.get(item_name, [])
        return [self._id_to_item[i] for i in ids]

    def get_all_items(self) -> List[Item]:
        return list(self._id_to_item.values())
