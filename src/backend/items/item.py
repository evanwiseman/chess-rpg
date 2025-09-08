from typing import List, Optional, Set
import copy
import json
import uuid


class Item:
    def __init__(
        self,
        name: str,
        description: str = "",
        max_quantity: int = 5,
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


class StackFullError(RuntimeError):
    def __init__(self, *args):
        super().__init__(*args)


class StackEmptyError(RuntimeError):
    def __init__(self, *args):
        super().__init__(*args)


class ItemStack:
    def __init__(self, items: List[Item]):
        self._max_quantity = self._validate_size(items)
        self._type_id = self._validate_type_id(items)
        self._ids = self._validate_ids(items)
        self._items: List[Item] = items.copy()

    # --- Helpers ---
    def _validate_size(self, items: List[Item]) -> int:
        """
        Checks if items are not empty or greater in size than max_quantity.
        Returns the max_quantity.
        Raise StackEmptyError if there are no items.
        Raise StackFullErorr if there are too many items.
        """
        if not items:
            raise StackEmptyError("ItemStack cannot be empty")
        if len(items) > items[0].max_quantity:
            raise StackFullError(
                f"ItemStack cannot exceed max quantity {items[0].max_quantity}"
            )
        return items[0].max_quantity

    def _validate_ids(self, items: List[Item]) -> Set[str]:
        """
        Check that items in the list are all unique.
        Return the set of ids if they're unique.
        Raise a KeyError if there is a duplicate.
        """
        ids = set()
        for item in items:
            if item.id in ids:
                raise KeyError(
                    "ItemStack requires unique ids for all items"
                )
        return ids

    def _validate_type_id(self, items: List[Item]):
        type_id = items[0].type_id
        for item in items:
            if item.type_id != type_id:
                raise ValueError(
                    "ItemStack requires same type_id for all items"
                )
        return type_id

    def is_empty(self) -> bool:
        """
        Check if there are no items in the stack.
        """
        return not self._items or len(self._items) == 0

    def has_space(self, quantity: int = 1) -> bool:
        """
        Return if True if there is enough space for quantity.
        """
        return quantity <= self.remaining

    # --- Properties ---
    @property
    def items(self) -> List[Item]:
        return self._items.copy()

    @property
    def ids(self) -> Set[str]:
        return self._ids

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
        return self._type_id

    # --- Operations ---
    def pop(self) -> Item:
        """
        Remove an item from the top of the stack.
        Raises a value error if the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        item = self._items.pop()
        self._ids.discard(item.id)
        return item

    def peek(self) -> Item:
        """
        Peek the last item added to the stack. Raises a value error if
        the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Cannot peek from an empty stack")
        return self._items[-1]

    def push(self, item: Item):
        """
        Add a single item to the stack. Raises StackFullError if full,
        or ValueError if item type doesn't match.
        """
        if item.type_id != self.type_id:
            raise ValueError("Item doesn't match stack")
        if item.id in self._ids:
            raise KeyError("Item is already in stack")
        if not self.has_space():
            raise StackFullError(f"Stack is full: max {self._max_quantity}")

        self._items.append(item)
        self._ids.add(item.id)

    def split(self, quantity: Optional[int] = None) -> 'ItemStack':
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

        split_items = []
        for _ in range(quantity):
            split_items.append(self.pop())
        return ItemStack(split_items)

    def can_merge(self, other: 'ItemStack') -> bool:
        return (
            self.type_id == other.type_id
            and self.quantity + other.quantity <= self.max_quantity
        )

    def merge(self, other: 'ItemStack') -> int:
        """
        Merge items from other stack into this one. Returns leftover count.
        """
        if self.type_id != other.type_id:
            raise ValueError("Cannot merge stacks of different types")
        available = self.remaining
        to_merge = min(available, other.quantity)
        for _ in range(to_merge):
            self.push(other.pop())
        return other.quantity  # leftover

    def clone(self):
        items = []
        for item in self._items:
            items.append(item.clone)
        return ItemStack(items)

    # --- Overrides ---
    def __iter__(self):
        yield from self._items

    def __len__(self):
        return self.quantity

    def __repr__(self):
        return (
            f"<ItemStack type={self.type_id[:8]} "
            f"quantity={self.quantity}/{self.max_quantity}>"
        )


class ItemSlot:
    def __init__(self, item_stack: Optional[ItemStack] = None):
        self.item_stack = item_stack
