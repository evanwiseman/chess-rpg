import unittest

from src.modifier import ModifierType, Modifier


class TestModifier(unittest.TestCase):
    def test_creation(self):
        modifier = Modifier("modifier", 1, ModifierType.FLAT, "source", 1)
        self.assertEqual(modifier.name, "modifier")
        self.assertEqual(modifier.value, 1)
        self.assertEqual(modifier.modifier_type, ModifierType.FLAT)
        self.assertEqual(modifier.source, "source")
        self.assertEqual(modifier.duration, 1)

    def test_apply_flat(self):
        modifier = Modifier("modifier", 1, ModifierType.FLAT)
        result = modifier.apply(1)
        self.assertEqual(result, 2)

    def test_apply_percentage(self):
        modifier = Modifier("modifier", 100, ModifierType.PERCENTAGE)
        result = modifier.apply(1)
        self.assertEqual(result, 2)

    def test_apply_multiplier(self):
        modifier = Modifier("modifier", 2, ModifierType.MULTIPLIER)
        result = modifier.apply(1)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
