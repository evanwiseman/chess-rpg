import copy

from typing import Dict, List, Optional, Union

from src.entities.items import Item


class ItemManager:
    def __init__(self):
        self._items: Dict[str, Item] = {}

    def _normalize_name(self, item: Union[Item, str]) -> str:
        """
        Convert slot EquipmentSlot or string to EquipmentSlot.

        Args:
            name: Items string name.

        Returns:
            string name as key to _items.
        """
        if isinstance(item, Item):
            return item.name.lower()
        elif isinstance(item, str):
            return item.lower()
        raise TypeError(
            "Item must be Item or string"
            f"got {type(item).__name__}"
        )

    def has_item(self, item: Union[Item, str]) -> bool:
        """
        Check if item exists in inventory.

        Args:
            name: Items string name.

        Returns:
            True of False if item name is in _items.
        """
        key = self._normalize_name(item)
        return key in self._items

    def get_item(self, item: Union[Item, str]) -> Optional[Item]:
        """
        Return item from a name.

        Args:
            name: Items string name.

        Returns:
            Item with matching name in _items
        """
        key = self._normalize_name(item)
        return self._items.get(key)

    def add_item(self, item: Union[Item, str]):
        """
        Add an item. Stacks if it already exists.

        Args:
            item: Item to add to _items.
        """
        key = self._normalize_name(item)
        if key not in self._items:
            self._items[key] = copy.deepcopy(item)
        else:
            self._items[key].quantity += item.quantity

    def remove_item(
        self,
        item: Union[Item, str],
        quantity: Optional[int] = None
    ) -> Optional[Item]:
        """
        Remove some or all of an item.

        Args:
            name: Items string name.
            quantity(optional): Amount of items to remove

        Returns:
            Removed item (deepcopy if partial).

        Raises:
            ValueError if quantity to remove is greater than items quantity.
        """
        key = self._normalize_name(item)
        item_to_remove = self._items.get(key)

        # Check item exists
        if not item_to_remove:
            return None

        # No quantity specified (remove entire item)
        if quantity is None:
            del self._items[key]
            return item_to_remove

        # Validate quantity
        if quantity <= 0:
            raise ValueError(f"Quantity must be positive, got {quantity}")

        # Check if enough items
        if quantity > item_to_remove.quantity:
            raise ValueError(
                f"Item '{item_to_remove.name}' cannot remove"
                f"({quantity}/{item.quantity})."
            )

        if quantity == item_to_remove.quantity:
            # Remove entire stack
            del self._items[key]
            return item_to_remove
        else:
            # Partial removal
            item_to_remove.quantity -= quantity
            removed_item = copy.deepcopy(item_to_remove)
            removed_item.quantity = quantity
            return removed_item

    def get_items(self) -> List[Item]:
        """
        Return a list of all Items
        """
        return list(self._items.values())

    def get_item_names(self) -> List[str]:
        """
        Return a list of all item names
        """
        return list[self._items.keys()]
