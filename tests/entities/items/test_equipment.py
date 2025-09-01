import unittest

from src.entities.items import Equipment, EquipmentSlot


class TestEquipment(unittest.TestCase):
    def test_creation(self):
        equipment = Equipment("equipment", EquipmentSlot.ARMOR)
        self.assertEqual(equipment.name, "equipment")
        self.assertEqual(equipment.is_alive, False)
        self.assertEqual(equipment.slot, EquipmentSlot.ARMOR)
        self.assertEqual(equipment.quantity, 1)
        self.assertGreaterEqual(equipment.id, 1)

    def test_modify(self):
        equipment = Equipment("equipment", EquipmentSlot.ARMOR)
        equipment.name = "armor"
        equipment.description = "this is armor"
        equipment.quantity = 2
        self.assertEqual(equipment.name, "armor")
        self.assertEqual(equipment.description, "this is armor")
        self.assertEqual(equipment.quantity, 2)


if __name__ == "__main__":
    unittest.main()
