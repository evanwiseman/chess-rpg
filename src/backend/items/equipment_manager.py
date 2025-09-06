from typing import Dict, List, Optional
from .equipment import Equipment, EquipmentSlot


class EquipmentManager:
    def __init__(self):
        # key = slot name; value = Equipment
        self._equipped: Dict[EquipmentSlot, Optional[Equipment]] = {
            slot: None for slot in EquipmentSlot
        }

    def is_slot_empty(self, slot: EquipmentSlot) -> bool:
        return self._equipped[slot] is None

    def get_equipment(self, slot: EquipmentSlot) -> Optional[Equipment]:
        return self._equipped.get(slot)

    def add_equipment(self, equipment: Equipment) -> Optional[Equipment]:
        return self.add_equipment_to_slot(equipment._slot, equipment)

    def add_equipment_to_slot(
        self,
        slot: EquipmentSlot,
        equipment: Equipment
    ) -> Optional[Equipment]:
        if equipment._slot != slot:
            raise ValueError(
                f"Equipment slot mismatch: expected '{slot.name}', "
                f"got '{equipment._slot.name}'"
            )

        previous_equipment = self._equipped[slot]
        self._equipped[slot] = equipment
        return previous_equipment

    def remove_equipment(self, equipment: Equipment) -> Optional[Equipment]:
        return self.remove_equipment_from_slot(equipment._slot)

    def remove_equipment_from_slot(
        self,
        slot: EquipmentSlot
    ) -> Optional[Equipment]:
        previous_equipment = self._equipped[slot]
        self._equipped[slot] = None
        return previous_equipment

    def get_equipped(self) -> Dict[EquipmentSlot, Optional[Equipment]]:
        return self._equipped.copy()

    def get_valid_slots(self) -> List[EquipmentSlot]:
        return list(EquipmentSlot)
