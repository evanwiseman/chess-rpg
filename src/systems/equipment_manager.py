from typing import Dict, List, Optional, Union

from src.entities.items import Equipment, EquipmentSlot


class EquipmentManager:
    def __init__(self):
        # key = slot name; value = Equipment
        self._equipped: Dict[EquipmentSlot, Optional[Equipment]] = {
            slot: None for slot in EquipmentSlot
        }

    def _normalize_slot(
        self,
        slot: Union[EquipmentSlot, str]
    ) -> EquipmentSlot:
        """
        Convert slot EquipmentSlot or string to EquipmentSlot.

        Args:
            slot: Either EquipmentSlot or string (name or value)

        Returns:
            EquipmentSlot enum as key to _equipped dict

        Raises:
            TypeError for invalid types.
            ValueError for invalid slot name/values.
        """
        if isinstance(slot, EquipmentSlot):
            return slot

        if not isinstance(slot, str):
            # Invalid type
            raise TypeError(
                f"Slot must be an EquipmentSlot/string,"
                f"got {type(slot).__name__}"
            )

        slot_upper = slot.upper()
        try:
            return EquipmentSlot[slot_upper]
        except KeyError:
            pass

        slot_lower = slot.lower()
        for equipment_slot in EquipmentSlot:
            if equipment_slot.value == slot_lower:
                return equipment_slot
        # If neither worked, raise error with helpful message
        valid_names = [slot.name for slot in EquipmentSlot]
        valid_values = [slot.value for slot in EquipmentSlot]
        raise ValueError(
            f"Invalid slot '{slot}'. Valid names: {valid_names}, "
            f"Valid values: {valid_values}"
        )

    def is_slot_empty(self, slot: Union[EquipmentSlot, str]) -> bool:
        """
        Check if a slot is empty.

        Args:
            slot: Either EquipmentSlot or string (name or value)

        Returns:
            True if slot is empty, False otherwise

        Raises:
            TypeError: slot is not EquipmentSlot or string
            ValueError: slot is invalid
        """
        normalized_slot = self._normalize_slot(slot)
        return self._equipped[normalized_slot] is None

    def get_equipment(
        self,
        slot: Union[EquipmentSlot, str]
    ) -> Optional[Equipment]:
        """
        Return Equipment in a slot.

        Args:
            slot: Either EquipmentSlot or string (name or value)

        Returns:
            Equipment in the slot, or None if empty

        Raises:
            TypeError: slot is not EquipmentSlot or string
            ValueError: slot is invalid
        """
        normalized_slot = self._normalize_slot(slot)
        equipment = self._equipped.get(normalized_slot)

        return equipment

    def add_equipment(
        self,
        slot: Union[EquipmentSlot, str],
        equipment: Equipment
    ) -> Optional[Equipment]:
        """
        Equip an Equipment into a slot.

        Args:
            slot: Either EquipmentSlot or string (name or value)
            equipment: Equipment to equip

        Returns:
            Previously equipped item, or None if slot was empty

        Raises:
            TypeError: slot is not EquipmentSlot or string
            ValueError: slot is invalid or equipment doesn't match slot
        """
        normalized_slot = self._normalize_slot(slot)

        if equipment.slot != normalized_slot:
            raise ValueError(
                f"Equipment slot mismatch: expected '{normalized_slot}', "
                f"got '{equipment.slot}'"
            )

        previous_equipment = self._equipped[normalized_slot]
        self._equipped[normalized_slot] = equipment
        return previous_equipment

    def remove_equipment(
        self,
        slot: Union[EquipmentSlot, str]
    ) -> Optional[Equipment]:
        """
        Unequip an item from a slot and return it.

        Args:
            slot: Either EquipmentSlot or string (name or value)

        Returns:
            Previously equipped item, or None if slot was empty

        Raises:
            TypeError: slot is not EquipmentSlot or string
            ValueError: slot is invalid or equipment doesn't match slot
        """
        normalized_slot = self._normalize_slot(slot)
        previous_equipment = self._equipped[normalized_slot]
        self._equipped[normalized_slot] = None
        return previous_equipment

    def get_equipped(self) -> Dict[EquipmentSlot, Optional[Equipment]]:
        """
        Return a dictionary of all slots and their equipped items.

        Returns:
            Copy of the equipped items dictionary
        """
        return self._equipped.copy()

    def get_equipped_items(self) -> List[Equipment]:
        """
        Return a list of all equipped items.

        Returns:
            List of all equipped items (excludes empty slots)
        """
        return [item for item in self._equipped.values() if item is not None]

    def get_valid_slots(self) -> List[EquipmentSlot]:
        """
        Return a list of all valid equipment slots.

        Returns:
            List of all EquipmentSlot enum values
        """
        return list(EquipmentSlot)
