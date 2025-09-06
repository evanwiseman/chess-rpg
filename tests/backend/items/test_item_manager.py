import unittest
from src.backend.items import ItemManager, Item, Equipment, EquipmentSlot


class TestItemManager(unittest.TestCase):
    def setUp(self):
        self.inventory = ItemManager(max_stacks=6)
        self.health_potion = Item("Health Potion", max_quantity=5)
        self.mana_potion = Item("Mana Potion", max_quantity=5)
        self.leather_armor = Equipment("Leather Armor", EquipmentSlot.ARMOR)
        self.ring = Equipment("Ring", EquipmentSlot.RING)

    # --- Add Item ---
    def test_add_item(self):
        self.inventory.add_item(self.health_potion)

        items = self.inventory.get_all_items()
        stacks = self.inventory.get_item_stacks(self.health_potion)

        # Validate items and stacks correct
        self.assertEqual(len(items), 1)
        self.assertEqual(len(stacks), 1)

        # Validate type ids get items
        type_id = self.health_potion.type_id
        health_potions = self.inventory.get_items_by_type_id(type_id)
        self.assertListEqual(health_potions, items)

    def test_add_multiple(self):
        self.inventory.add_item(self.health_potion, 3)
        items = self.inventory.get_all_items()
        stacks = self.inventory.get_all_stacks()

        self.assertEqual(len(items), 3)
        self.assertEqual(len(stacks), 1)

        self.inventory.add_item(self.mana_potion, 3)
        items = self.inventory.get_all_items()
        stacks = self.inventory.get_all_stacks()

        # Check items and stacks updated
        self.assertEqual(len(items), 6)
        self.assertEqual(len(stacks), 2)

        # Check that all uuids are unique
        ids = set([item.id for item in items])
        self.assertEqual(len(ids), len(items))

    def test_add_overflow(self):
        self.inventory.add_item(self.health_potion, 3)
        self.inventory.add_item(self.health_potion, 3)

        items = self.inventory.get_all_items()
        stacks = self.inventory.get_all_stacks()

        self.assertEqual(len(items), 6)
        self.assertEqual(len(stacks), 2)

    def test_add_zero(self):
        # Can't add zero should raise
        with self.assertRaises(ValueError):
            self.inventory.add_item(self.health_potion, 0)

    def test_add_over_max_quantity(self):
        self.inventory.add_item(self.health_potion, 6)

        items = self.inventory.get_all_items()
        stacks = self.inventory.get_all_stacks()

        self.assertEqual(len(items), 6)
        self.assertEqual(len(stacks), 2)

    # --- Remove Item ---
    def test_remove_item(self):
        self.inventory.add_item(self.health_potion)
        self.inventory.remove_item(self.health_potion)

        items = self.inventory.get_all_items()
        stacks = self.inventory.get_all_stacks()

        # All items and stacks should be removed
        self.assertEqual(len(items), 0)
        self.assertEqual(len(stacks), 0)

    def test_remove_multiple(self):
        self.inventory.add_item(self.health_potion, 3)
        self.inventory.remove_item(self.health_potion, 2)

        items = self.inventory.get_all_items()
        stacks = self.inventory.get_all_stacks()

        # Check for correct size
        self.assertEqual(len(items), 1)
        self.assertEqual(len(stacks), 1)

        ids = set([item.id for item in items])
        self.assertEqual(len(ids), len(items))

    def test_remove_overflow(self):
        self.inventory.add_item(self.health_potion, 1)
        self.inventory.remove_item(self.health_potion, 1)
        with self.assertRaises(ValueError):
            self.inventory.remove_item(self.health_potion, 1)

        items = self.inventory.get_all_items()
        stacks = self.inventory.get_all_stacks()

        self.assertEqual(len(items), 0)
        self.assertEqual(len(stacks), 0)

    def test_remove_over_max(self):
        self.inventory.add_item(self.health_potion, 1)

        with self.assertRaises(ValueError):
            self.inventory.remove_item(self.health_potion, 2)

        items = self.inventory.get_all_items()
        stacks = self.inventory.get_all_stacks()

        self.assertEqual(len(items), 1)
        self.assertEqual(len(stacks), 1)

    # --- Lookup ---
    def test_has_item(self):
        self.inventory.add_item(self.health_potion, 2)
        self.assertTrue(self.inventory.has_item("Health Potion", 2))
        self.assertFalse(self.inventory.has_item("Health Potion", 5))

    # --- Stack management ---
    def test_move_stack_changes_order(self):
        self.inventory.add_item(self.health_potion, 5)  # full stack
        self.inventory.add_item(self.mana_potion, 2)   # second stack
        stacks = self.inventory.get_all_stacks()
        self.inventory.move_stack(stacks[0], 1)
        new_order = self.inventory.get_all_stacks()
        self.assertEqual(new_order[1].type_id, stacks[0].type_id)

    def test_swap_stack_and_by_index(self):
        self.inventory.add_item(self.health_potion, 5)
        self.inventory.add_item(self.mana_potion, 2)
        stacks = self.inventory.get_all_stacks()
        self.inventory.swap_stack(stacks[0], stacks[1])
        self.assertEqual(self.inventory.get_all_stacks()[0], stacks[1])

        # swap back by index
        self.inventory.swap_stack_by_index(0, 1)
        self.assertEqual(self.inventory.get_all_stacks()[0], stacks[0])

    def test_swap_invalid_index_raises(self):
        with self.assertRaises(IndexError):
            self.inventory.swap_stack_by_index(0, 5)

    # --- Split ---
    def test_split_stack_creates_new_stack(self):
        self.inventory.add_item(self.health_potion, 4)
        stack = self.inventory.get_item_stacks(self.health_potion)[0]
        new_stack = self.inventory.split_stack(stack, 2)
        self.assertEqual(stack.quantity, 2)
        self.assertEqual(new_stack.quantity, 2)
        self.assertIn(new_stack, self.inventory.get_all_stacks())

    def test_split_stack_default_half(self):
        self.inventory.add_item(self.health_potion, 5)
        stack = self.inventory.get_item_stacks(self.health_potion)[0]
        new_stack = self.inventory.split_stack(stack)  # default half
        self.assertEqual(stack.quantity + new_stack.quantity, 5)

    def test_split_invalid_quantity_raises(self):
        self.inventory.add_item(self.health_potion, 2)
        stack = self.inventory.get_item_stacks(self.health_potion)[0]
        with self.assertRaises(ValueError):
            self.inventory.split_stack(stack, 0)
        with self.assertRaises(ValueError):
            self.inventory.split_stack(stack, 5)

    def test_split_stack_inventory_full_raises(self):
        # Fill inventory to max_stacks
        self.inventory.add_item(self.health_potion, 30)  # 6 stacks of 5
        stack = self.inventory.get_item_stacks(self.health_potion)[0]
        with self.assertRaises(RuntimeError):
            self.inventory.split_stack(stack, 1)


if __name__ == "__main__":
    unittest.main()
