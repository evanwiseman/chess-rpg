import unittest
from src.backend.items import Item


class TestItem(unittest.TestCase):
    def setUp(self):
        self.item_name = "Health Potion"
        self.item_desc = "Restores health"
        self.max_qty = 5
        self.item = Item(
            name=self.item_name,
            description=self.item_desc,
            max_quantity=self.max_qty
        )

    def test_creation(self):
        self.assertEqual(self.item.name, self.item_name)
        self.assertEqual(self.item.description, self.item_desc)
        self.assertEqual(self.item.max_quantity, self.max_qty)
        self.assertIsInstance(self.item.id, str)
        self.assertEqual(len(self.item.id), 32)  # hex UUID length

    def test_type_id_consistency(self):
        item2 = Item(
            name=self.item_name,
            description=self.item_desc,
            max_quantity=self.max_qty
        )
        # type_id should be identical for same name/max_quantity
        self.assertEqual(self.item.type_id, item2.type_id)
        # Different name gives different type_id
        item3 = Item(
            name="Mana Potion",
            description=self.item_desc,
            max_quantity=self.max_qty
        )
        self.assertNotEqual(self.item.type_id, item3.type_id)

    def test_clone_creates_new_uuid(self):
        clone = self.item.clone()
        self.assertIsInstance(clone, Item)
        self.assertNotEqual(clone.id, self.item.id)
        self.assertEqual(clone.name, self.item.name)
        self.assertEqual(clone.description, self.item.description)
        self.assertEqual(clone.max_quantity, self.item.max_quantity)
        # type_id should still match
        self.assertEqual(clone.type_id, self.item.type_id)

    def test_equality(self):
        clone = self.item.clone()
        self.assertNotEqual(self.item, clone)
        self.assertEqual(self.item, self.item)

    def test_repr(self):
        repr_str = repr(self.item)
        self.assertIn(self.item.name, repr_str)
        self.assertIn(self.item.id, repr_str)


if __name__ == "__main__":
    unittest.main()
