import unittest
from src.backend.items import Item, ItemStack, StackFullError


class TestItemStack(unittest.TestCase):
    def setUp(self):
        self.item = Item(name="Health Potion", max_quantity=5)
        self.stack = ItemStack([self.item])

    def test_initialization(self):
        # Single item stack
        self.assertEqual(self.stack.quantity, 1)
        self.assertEqual(self.stack.max_quantity, self.item.max_quantity)
        self.assertEqual(self.stack.type_id, self.item.type_id)

        # Creating stack with multiple items
        items = [self.item.clone() for _ in range(3)]
        multi_stack = ItemStack(items)
        self.assertEqual(multi_stack.quantity, 3)

        # Should raise if items have different type_id
        other_item = Item(name="Mana Potion", max_quantity=5)
        with self.assertRaises(ValueError):
            ItemStack([self.item, other_item])

        # Should raise if empty list
        with self.assertRaises(ValueError):
            ItemStack([])

    def test_push_pop_peek(self):
        # Push items until full
        while self.stack.has_space():
            self.stack.push_item(self.item.clone())
        self.assertEqual(self.stack.quantity, self.stack.max_quantity)
        # Pushing beyond max raises
        with self.assertRaises(StackFullError):
            self.stack.push_item(self.item.clone())

        # Peek returns the last item but does not remove
        top_item = self.stack.peek_item()
        self.assertEqual(top_item, self.stack.items[-1])
        self.assertEqual(self.stack.quantity, self.stack.max_quantity)

        # Pop removes an item
        popped = self.stack.pop_item()
        self.assertEqual(popped, top_item)
        self.assertEqual(self.stack.quantity, self.stack.max_quantity - 1)

        # Pop until empty
        while not self.stack.is_empty():
            self.stack.pop_item()
        with self.assertRaises(ValueError):
            self.stack.pop_item()
        with self.assertRaises(ValueError):
            self.stack.peek_item()

    def test_has_space(self):
        self.assertTrue(self.stack.has_space())
        for _ in range(self.stack.max_quantity - 1):
            self.stack.push_item(self.item.clone())
        self.assertFalse(self.stack.has_space())

    def test_split_stack(self):
        # Add items to stack
        items = [self.item.clone() for _ in range(4)]
        stack = ItemStack([self.item] + items)
        self.assertEqual(stack.quantity, 5)

        # Split by quantity
        split = stack.split_stack(2)
        self.assertEqual(split.quantity, 2)
        self.assertEqual(stack.quantity, 3)

        # Split more than quantity returns whole stack
        split_all = stack.split_stack(10)
        self.assertEqual(split_all.quantity, 3)
        self.assertTrue(stack.is_empty())

        # Split with None splits roughly half
        items2 = [self.item.clone() for _ in range(4)]
        stack2 = ItemStack([self.item] + items2)
        half_stack = stack2.split_stack()
        self.assertEqual(half_stack.quantity, stack2.max_quantity // 2)

    def test_repr(self):
        rep = repr(self.stack)
        self.assertIn(self.stack.type_id[:8], rep)
        self.assertIn(str(self.stack.quantity), rep)
        self.assertIn(str(self.stack.max_quantity), rep)


if __name__ == "__main__":
    unittest.main()
