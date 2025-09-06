from typing import List, Optional
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
        self._typeid = items[0].type_id
        for item in items:
            if item.type_id != self._typeid:
                raise ValueError("All items in stack must be identical")

        self._items: List[Item] = items.copy()

    @property
    def items(self) -> List[Item]:
        return self._items.copy()

    @property
    def quantity(self) -> int:
        return len(self._items)

    @property
    def max_quantity(self) -> int:
        return self._max_quantity

    @property
    def remaining(self) -> int:
        return self.max_quantity - self.quantity

    @property
    def type_id(self) -> str:
        return self._typeid

    def is_empty(self) -> bool:
        """
        Check if there are no items in the stack.
        """
        return len(self._items) == 0

    def has_space(self, quantity: int = 1) -> bool:
        """
        Return if True if there is enough space for quantity.
        """
        return quantity <= self.remaining

    def get_items(self) -> List[Item]:
        return self._items

    def pop_item(self) -> Item:
        """
        Remove an item from the top of the stack. Raises a value
        error if the stack is empty.
        """
        if not self._items:
            raise ValueError("Cannot pop from an empty stack")
        return self._items.pop()

    def peek_item(self) -> Item:
        """
        Peek the last item added to the stack. Raises a value error if
        the stack is empty.
        """
        if not self._items:
            raise ValueError("Cannot peek from an empty stack")
        return self._items[-1]

    def push_item(self, item: Item):
        """
        Add a single item to the stack. Raises StackFullError if full,
        or ValueError if item type doesn't match.
        """
        if item.type_id != self._typeid:
            raise ValueError("Item doesn't match stack")
        if self.has_space():
            self._items.append(item)
        else:
            raise StackFullError(f"Stack is full: max {self._max_quantity}")

    def split_stack(self, quantity: Optional[int] = None) -> 'ItemStack':
        """
        Split the stack by a specified quantity. If the quantity is not
        specified will try to split in half. Returns a new ItemStack.
        """
        if quantity is None:  # Try to split in half if not specified
            quantity = self.max_quantity // 2
        if quantity < 1:
            raise ValueError("Cannot split into an empty stack")
        if quantity >= self.quantity:
            new_stack = ItemStack(self._items.copy())
            self._items.clear()
            return new_stack

        split_items = self._items[-quantity:]
        self._items = self._items[:-quantity]
        return ItemStack(split_items)

    def __repr__(self):
        return (
            f"<ItemStack type={self._typeid[:8]} "
            f"quantity={self.quantity}/{self.max_quantity}>"
        )
