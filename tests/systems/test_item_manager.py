import unittest

from src.entities.items import Item
from src.systems import ItemManager


class TestEquipmentManager(unittest.TestCase):
    def test_creation(self):
        item_manager = ItemManager()
        self.assertIsInstance(item_manager, ItemManager)

    def test_add_item(self):
        item_manager = ItemManager()

        item = Item("item")
        item_manager.add_item(item)

        self.assertEqual(item_manager.get_item("item"), item)

    def test_remove_item_str(self):
        item_manager = ItemManager()

        item = Item("item")
        item_manager.add_item(item)
        item_manager.remove_item("item")

        self.assertIsNone(item_manager.get_item("item"))

    def test_remove_item(self):
        item_manager = ItemManager()

        item = Item("item")
        item_manager.add_item(item)
        item_manager.remove_item(item)

        self.assertIsNone(item_manager.get_item(item))

    def test_add_multiple_items(self):
        item_manager = ItemManager()

        item1 = Item("item1")
        item_manager.add_item(item1)

        item2 = Item("item2")
        item_manager.add_item(item2)

        item3 = Item("item3")
        item_manager.add_item(item3)

        item4 = Item("item4")
        item_manager.add_item(item4)

        item5 = Item("item5")
        item_manager.add_item(item5)

        self.assertListEqual(
            item_manager.get_items(),
            [
                item1,
                item2,
                item3,
                item4,
                item5
            ]
        )

    def test_remove_multiple_items_str(self):
        item_manager = ItemManager()

        item1 = Item("item1")
        item_manager.add_item(item1)

        item2 = Item("item2")
        item_manager.add_item(item2)

        item3 = Item("item3")
        item_manager.add_item(item3)

        item4 = Item("item4")
        item_manager.add_item(item4)

        item5 = Item("item5")
        item_manager.add_item(item5)

        item_manager.remove_item("item1")
        item_manager.remove_item("item2")
        item_manager.remove_item("item3")
        item_manager.remove_item("item4")
        item_manager.remove_item("item5")

        self.assertListEqual(
            item_manager.get_items(),
            []
        )

    def test_remove_multiple_items(self):
        item_manager = ItemManager()

        item1 = Item("item1")
        item_manager.add_item(item1)

        item2 = Item("item2")
        item_manager.add_item(item2)

        item3 = Item("item3")
        item_manager.add_item(item3)

        item4 = Item("item4")
        item_manager.add_item(item4)

        item5 = Item("item5")
        item_manager.add_item(item5)

        item_manager.remove_item(item1)
        item_manager.remove_item(item2)
        item_manager.remove_item(item3)
        item_manager.remove_item(item4)
        item_manager.remove_item(item5)

        self.assertListEqual(
            item_manager.get_items(),
            []
        )


if __name__ == "__main__":
    unittest.main()
