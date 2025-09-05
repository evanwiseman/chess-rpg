from typing import List
from .item import Item


class StackFullError(Exception):
    pass


class ItemStack:
    def __init__(self, items: List[Item]):
        # Validate size
        if not items:
            raise ValueError("ItemStack cannot be empty")
        self._max_quantity = items[0].max_quantity
        if len(items) > self._max_quantity:
            raise ValueError(
                f"Cannot exceed max quantity {self._max_quantity}"
            )

        # Validate initial stack
        self._typeid = items[0].type_id()
        for item in items:
            if item.type_id() != self._typeid:
                raise ValueError("All items in stack must be identical")

        self._items: List[Item] = items.copy()

    @property
    def quantity(self) -> int:
        return len(self._items)

    @property
    def max_quantity(self) -> int:
        return self._max_quantity

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def has_space(self) -> bool:
        return self.quantity < self.max_quantity

    def pop_item(self) -> Item:
        if not self._items:
            raise ValueError("Cannot pop from an empty stack")
        return self._items.pop()

    def peek_item(self) -> Item:
        if not self._items:
            raise ValueError("Cannot peek from an empty stack")
        return self._items[-1]

    def push_item(self, item: Item):
        if item.type_id() != self._typeid:
            raise ValueError("Item doesn't match stack")
        if self.has_space():
            self._items.append(item)
        else:
            raise StackFullError(f"Stack is full: max {self._max_quantity}")

    def split_stack(self, quantity: int) -> 'ItemStack':
        if quantity < 1:
            raise ValueError("Cannot split into an empty stack")
        if quantity >= self.quantity:
            # Copy the entire stack
            new_stack = ItemStack(self._items.copy())
            self._items.clear()
            return new_stack

        # Otherwise, pop the requested quantity
        split_items = [self.pop_item() for _ in range(quantity)]
        return ItemStack(split_items)
