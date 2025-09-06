from collections import defaultdict
from typing import Dict, List, Optional
from .item import Item
from .item_stack import ItemStack


class ItemManager:
    def __init__(self, max_stacks: int = 6):
        # Track every item instance by unique ID
        self._id_to_item: Dict[str, Item] = {}

        # Name -> list of item IDs (for UI/lookup)
        self._name_to_ids: Dict[str, List[int]] = defaultdict(list)

        # TypeID -> list of ItemStacks
        self._type_id_to_stacks: Dict[str, List[ItemStack]] = defaultdict(list)

        # Master ordered list to keep track of all stacks (for GUI)
        self._all_stacks: List[ItemStack] = []

        self.max_stacks = max_stacks

    # --- Helpers ---
    def _get_type_id(self, item: Item) -> str:
        return item.type_id

    def _register_stack(self, item_stack: ItemStack):
        self._type_id_to_stacks[item_stack.type_id].append(item_stack)
        self._all_stacks.append(item_stack)

    def _register_item(self, item: Item):
        """Helper to register item in ID and name mappings."""
        self._id_to_item[item.id] = item
        self._name_to_ids[item.name].append(item.id)

    def _unregister_item(self, item: Item):
        """Helper to remove an item from ID and name mappings."""
        self._id_to_item.pop(item.id, None)
        ids = self._name_to_ids.get(item.name)
        if ids:
            try:
                ids.remove(item.id)
            except ValueError:
                pass
            if not ids:
                self._name_to_ids.pop(item.name)

    def _unregister_stack(self, item_stack: ItemStack):
        stacks = self._type_id_to_stacks.get(item_stack.type_id)
        if stacks:
            try:
                stacks.remove(item_stack)
            except ValueError:
                pass
            if not stacks:
                self._type_id_to_stacks.pop(item_stack.type_id, None)
        try:
            self._all_stacks.remove(item_stack)
        except ValueError:
            pass

    # -- Item Operations ---
    def add_item(self, item: Item, quantity: int = 1):
        """Add quantity of an item, splitting across stacks if needed."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        type_id = self._get_type_id(item)
        remaining = quantity

        # Fill existing stacks first
        for stack in self._type_id_to_stacks[type_id]:
            to_add = min(stack.remaining, remaining)
            for _ in range(to_add):
                new_item = item.clone()
                stack.push_item(new_item)
                self._register_item(new_item)
            remaining -= to_add
            if remaining <= 0:
                break

        # Create new stacks if needed
        while remaining > 0:
            if len(self._all_stacks) >= self.max_stacks:
                raise RuntimeError(
                    f"Cannot add item: inventory full ({self.max_stacks} slots)"
                )

            stack_size = min(item.max_quantity, remaining)
            new_items = [item.clone() for _ in range(stack_size)]
            new_stack = ItemStack(new_items)

            self._register_stack(new_stack)
            for new_item in new_items:
                self._register_item(new_item)
            remaining -= stack_size

    def remove_item(self, item: Item, quantity: int = 1) -> List[Item]:
        """Remove quantity of items by instance type."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        available_ids = self._name_to_ids.get(item.name, [])
        if len(available_ids) < quantity:
            raise ValueError(f"Cannot remove {quantity} {item.name}(s)")

        removed_items: List[Item] = []
        type_id = self._get_type_id(item)
        stacks = self._type_id_to_stacks.get(type_id, [])
        remaining = quantity
        for stack in reversed(stacks[:]):
            while not stack.is_empty() and remaining > 0:
                top_item = stack.pop_item()
                removed_items.append(top_item)
                self._unregister_item(top_item)
                remaining -= 1
            if stack.is_empty():
                self._unregister_stack(stack)

            if remaining <= 0:
                break

        if remaining > 0:
            raise RuntimeError("Unexpected: Not enough items removed")

        # Clean up empty stacks dictionary
        if not stacks:
            self._type_id_to_stacks.pop(type_id, None)

        return removed_items

    def get_item_quantity(self, item: Item) -> int:
        """Return total quantity of an item by name."""
        type_id = self._get_type_id(item)
        item_stacks = self._type_id_to_stacks.get(type_id, [])
        return sum([item_stack.quantity for item_stack in item_stacks])

    def get_items_by_name(self, item_name: str) -> List[Item]:
        """Return all items with the given name."""
        return [
            self._id_to_item[i] for i in self._name_to_ids.get(item_name, [])
        ]

    def get_items_by_type_id(self, type_id: str) -> List[Item]:
        """
        Return all Items matching a type_id
        """
        stacks = self._type_id_to_stacks.get(type_id, [])
        items = []
        for stack in stacks:
            items.extend(stack.get_items())
        return items

    def get_all_items(self) -> List[Item]:
        """Return all items managed by this manager."""
        return list(self._id_to_item.values())

    def has_item(self, item_name: str, quantity: int = 1) -> bool:
        """Check if we have at least `quantity` items by name."""
        return len(self._name_to_ids.get(item_name, [])) >= quantity

    # --- Stack Operations ---
    def get_item_stacks(self, item: Item) -> List[ItemStack]:
        """Return all stacks of a specific item type."""
        type_id = self._get_type_id(item)
        return self._type_id_to_stacks.get(type_id, [])

    def get_all_stacks(self) -> List[ItemStack]:
        return self._all_stacks.copy()

    def move_stack(self, stack: ItemStack, new_index: int):
        """Move a stack to a new index in the inventory list (GUI)."""
        if stack not in self._all_stacks:
            raise ValueError("Stack not in inventory")
        self._all_stacks.remove(stack)
        self._all_stacks.insert(new_index, stack)

    def swap_stack(self, stack1: ItemStack, stack2: ItemStack):
        if stack1 not in self._all_stacks or stack2 not in self._all_stacks:
            raise ValueError("Stacks not in inventory")

        index1 = self._all_stacks.index(stack1)
        index2 = self._all_stacks.index(stack2)

        self.swap_stack_by_index(index1, index2)

    def swap_stack_by_index(self, index1, index2):
        if index1 >= len(self._all_stacks) or index1 < 0:
            raise IndexError(f"Index {index1} is out of range.")
        if index2 >= len(self._all_stacks) or index2 < 0:
            raise IndexError(f"Index {index1} is out of range.")

        self._all_stacks[index1], self._all_stacks[index2] = (
            self._all_stacks[index2], self._all_stacks[index1]
        )

    def split_stack(
        self,
        item_stack: ItemStack,
        quantity: Optional[int] = None
    ) -> ItemStack:
        """
        Split `quantity` items from the given stack into a new stack.
        Updates ID and name mappings for the new items.
        If quantity is None split stack in half.
        """
        if len(self._all_stacks) >= self.max_stacks:
            raise RuntimeError(
                f"Cannot split stack: inventory full ({self.max_stacks} slots)"
            )

        item_stacks = self._type_id_to_stacks.get(item_stack.type_id, [])
        if item_stack not in item_stacks:
            raise ValueError("Stack not managed by this ItemManager")

        if quantity and (quantity <= 0 or quantity > item_stack.quantity):
            raise ValueError("Invalid split quantity")

        new_stack = item_stack.split_stack(quantity)

        # Add the new stack to the manager
        self._type_id_to_stacks[item_stack.type_id].append(new_stack)
        self._all_stacks.append(new_stack)
        return new_stack
