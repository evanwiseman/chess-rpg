import unittest

from src.entities.items import Item


class TestItem(unittest.TestCase):
    def test_creation(self):
        item = Item("item")
        self.assertIsInstance(item, Item)
        self.assertGreaterEqual(item.id, 1)
        self.assertEqual(item.name, "item")
        self.assertEqual(item.description, "description")
        self.assertEqual(item.is_alive, False)

    def test_modify(self):
        item = Item("item")
        item.name = "helmet"
        item.description = "this is a helmet"
        item.quantity = 3
        self.assertEqual(item.name, "helmet")
        self.assertEqual(item.description, "this is a helmet")
        self.assertEqual(item.quantity, 3)


if __name__ == "__main__":
    unittest.main()
