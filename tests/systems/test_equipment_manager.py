import unittest

from src.entities.items import Equipment, EquipmentSlot
from src.systems import EquipmentManager


class TestEquipmentManager(unittest.TestCase):
    def test_creation(self):
        equipment_manager = EquipmentManager()
        self.assertIsInstance(equipment_manager, EquipmentManager)

    def test_slot_empty(self):
        equipment_manager = EquipmentManager()
        self.assertTrue(equipment_manager.is_slot_empty(EquipmentSlot.ARMOR))

    def test_add_equipment(self):
        equipment_manager = EquipmentManager()

        armor = Equipment("Leather Armor", EquipmentSlot.ARMOR)
        previous = equipment_manager.add_equipment(EquipmentSlot.ARMOR, armor)

        self.assertIsNone(previous, None)
        self.assertEqual(
            equipment_manager.get_equipment(EquipmentSlot.ARMOR),
            armor
        )

    def test_remove_equipement(self):
        equipment_manager = EquipmentManager()

        armor = Equipment("Leather Armor", EquipmentSlot.ARMOR)
        equipment_manager.add_equipment(EquipmentSlot.ARMOR, armor)

        previous = equipment_manager.remove_equipment(EquipmentSlot.ARMOR)

        self.assertEqual(previous, armor)
        self.assertIsNone(equipment_manager.get_equipment(EquipmentSlot.ARMOR))

    def test_add_all_slots(self):
        equipment_manager = EquipmentManager()

        helmet = Equipment("Leather Helmet", EquipmentSlot.HELMET)
        equipment_manager.add_equipment(EquipmentSlot.HELMET, helmet)

        armor = Equipment("Leather Armor", EquipmentSlot.ARMOR)
        equipment_manager.add_equipment(EquipmentSlot.ARMOR, armor)

        gloves = Equipment("Leather Gloves", EquipmentSlot.GLOVES)
        equipment_manager.add_equipment(EquipmentSlot.GLOVES, gloves)

        legs = Equipment("Leather Pants", EquipmentSlot.LEGS)
        equipment_manager.add_equipment(EquipmentSlot.LEGS, legs)

        boots = Equipment("Leather Boots", EquipmentSlot.BOOTS)
        equipment_manager.add_equipment(EquipmentSlot.BOOTS, boots)

        ring = Equipment("Ring of Health", EquipmentSlot.RING)
        equipment_manager.add_equipment(EquipmentSlot.RING, ring)

        necklace = Equipment("Necklace of Mana", EquipmentSlot.NECKLACE)
        equipment_manager.add_equipment(EquipmentSlot.NECKLACE, necklace)

        self.assertEqual(
            equipment_manager.get_equipment(EquipmentSlot.HELMET),
            helmet
        )
        self.assertEqual(
            equipment_manager.get_equipment(EquipmentSlot.ARMOR),
            armor
        )
        self.assertEqual(
            equipment_manager.get_equipment(EquipmentSlot.GLOVES),
            gloves
        )
        self.assertEqual(
            equipment_manager.get_equipment(EquipmentSlot.LEGS),
            legs
        )
        self.assertEqual(
            equipment_manager.get_equipment(EquipmentSlot.BOOTS),
            boots
        )
        self.assertEqual(
            equipment_manager.get_equipment(EquipmentSlot.RING),
            ring
        )
        self.assertEqual(
            equipment_manager.get_equipment(EquipmentSlot.NECKLACE),
            necklace
        )

    def test_remove_all_slots(self):
        equipment_manager = EquipmentManager()

        helmet = Equipment("Leather Helmet", EquipmentSlot.HELMET)
        equipment_manager.add_equipment(EquipmentSlot.HELMET, helmet)

        armor = Equipment("Leather Armor", EquipmentSlot.ARMOR)
        equipment_manager.add_equipment(EquipmentSlot.ARMOR, armor)

        gloves = Equipment("Leather Gloves", EquipmentSlot.GLOVES)
        equipment_manager.add_equipment(EquipmentSlot.GLOVES, gloves)

        legs = Equipment("Leather Pants", EquipmentSlot.LEGS)
        equipment_manager.add_equipment(EquipmentSlot.LEGS, legs)

        boots = Equipment("Leather Boots", EquipmentSlot.BOOTS)
        equipment_manager.add_equipment(EquipmentSlot.BOOTS, boots)

        ring = Equipment("Ring of Health", EquipmentSlot.RING)
        equipment_manager.add_equipment(EquipmentSlot.RING, ring)

        necklace = Equipment("Necklace of Mana", EquipmentSlot.NECKLACE)
        equipment_manager.add_equipment(EquipmentSlot.NECKLACE, necklace)

        equipment_manager.remove_equipment(EquipmentSlot.HELMET)
        equipment_manager.remove_equipment(EquipmentSlot.ARMOR)
        equipment_manager.remove_equipment(EquipmentSlot.GLOVES)
        equipment_manager.remove_equipment(EquipmentSlot.LEGS)
        equipment_manager.remove_equipment(EquipmentSlot.BOOTS)
        equipment_manager.remove_equipment(EquipmentSlot.RING)
        equipment_manager.remove_equipment(EquipmentSlot.NECKLACE)

        self.assertIsNone(
            equipment_manager.get_equipment(EquipmentSlot.HELMET)
        )
        self.assertIsNone(
            equipment_manager.get_equipment(EquipmentSlot.ARMOR)
        )
        self.assertIsNone(
            equipment_manager.get_equipment(EquipmentSlot.GLOVES)
        )
        self.assertIsNone(
            equipment_manager.get_equipment(EquipmentSlot.LEGS)
        )
        self.assertIsNone(
            equipment_manager.get_equipment(EquipmentSlot.BOOTS)
        )
        self.assertIsNone(
            equipment_manager.get_equipment(EquipmentSlot.RING)
        )
        self.assertIsNone(
            equipment_manager.get_equipment(EquipmentSlot.NECKLACE)
        )

    def test_get_equipped(self):
        equipment_manager = EquipmentManager()

        helmet = Equipment("Leather Helmet", EquipmentSlot.HELMET)
        equipment_manager.add_equipment(EquipmentSlot.HELMET, helmet)

        armor = Equipment("Leather Armor", EquipmentSlot.ARMOR)
        equipment_manager.add_equipment(EquipmentSlot.ARMOR, armor)

        gloves = Equipment("Leather Gloves", EquipmentSlot.GLOVES)
        equipment_manager.add_equipment(EquipmentSlot.GLOVES, gloves)

        legs = Equipment("Leather Pants", EquipmentSlot.LEGS)
        equipment_manager.add_equipment(EquipmentSlot.LEGS, legs)

        boots = Equipment("Leather Boots", EquipmentSlot.BOOTS)
        equipment_manager.add_equipment(EquipmentSlot.BOOTS, boots)

        ring = Equipment("Ring of Health", EquipmentSlot.RING)
        equipment_manager.add_equipment(EquipmentSlot.RING, ring)

        necklace = Equipment("Necklace of Mana", EquipmentSlot.NECKLACE)
        equipment_manager.add_equipment(EquipmentSlot.NECKLACE, necklace)

        self.assertDictEqual(
            equipment_manager.get_equipped(),
            {
                EquipmentSlot.HELMET: helmet,
                EquipmentSlot.ARMOR: armor,
                EquipmentSlot.GLOVES: gloves,
                EquipmentSlot.LEGS: legs,
                EquipmentSlot.BOOTS: boots,
                EquipmentSlot.RING: ring,
                EquipmentSlot.NECKLACE: necklace
            }
        )

    def test_get_equipped_items(self):
        equipment_manager = EquipmentManager()

        helmet = Equipment("Leather Helmet", EquipmentSlot.HELMET)
        equipment_manager.add_equipment(EquipmentSlot.HELMET, helmet)

        armor = Equipment("Leather Armor", EquipmentSlot.ARMOR)
        equipment_manager.add_equipment(EquipmentSlot.ARMOR, armor)

        gloves = Equipment("Leather Gloves", EquipmentSlot.GLOVES)
        equipment_manager.add_equipment(EquipmentSlot.GLOVES, gloves)

        legs = Equipment("Leather Pants", EquipmentSlot.LEGS)
        equipment_manager.add_equipment(EquipmentSlot.LEGS, legs)

        boots = Equipment("Leather Boots", EquipmentSlot.BOOTS)
        equipment_manager.add_equipment(EquipmentSlot.BOOTS, boots)

        ring = Equipment("Ring of Health", EquipmentSlot.RING)
        equipment_manager.add_equipment(EquipmentSlot.RING, ring)

        necklace = Equipment("Necklace of Mana", EquipmentSlot.NECKLACE)
        equipment_manager.add_equipment(EquipmentSlot.NECKLACE, necklace)

        self.assertListEqual(
            equipment_manager.get_equipped_items(),
            [
                helmet,
                armor,
                gloves,
                legs,
                boots,
                ring,
                necklace
            ]
        )

    def test_get_valid_slots(self):
        equipment_manager = EquipmentManager()
        self.assertListEqual(
            equipment_manager.get_valid_slots(),
            [
                EquipmentSlot.HELMET,
                EquipmentSlot.ARMOR,
                EquipmentSlot.GLOVES,
                EquipmentSlot.LEGS,
                EquipmentSlot.BOOTS,
                EquipmentSlot.RING,
                EquipmentSlot.NECKLACE
            ]
        )


if __name__ == "__main__":
    unittest.main()
