import unittest
from src.backend.stats import Modifier, ModifierType


class TestModifier(unittest.TestCase):
    def setUp(self):
        # Common modifiers for use in tests
        self.flat_mod = Modifier(
            name="Flat Boost",
            value=10,
            modifier_type=ModifierType.FLAT
        )
        self.percent_mod = Modifier(
            name="Percent Boost",
            value=20,
            modifier_type=ModifierType.PERCENTAGE
        )
        self.mult_mod = Modifier(
            name="Multiplier Boost",
            value=1.5,
            modifier_type=ModifierType.MULTIPLIER
        )
        self.temp_mod = Modifier(
            name="Temporary Boost",
            value=5,
            modifier_type=ModifierType.FLAT,
            duration=2
        )

    # --- Test apply() ---
    def test_apply_flat(self):
        self.assertEqual(self.flat_mod.apply(100), 110)

    def test_apply_percentage(self):
        self.assertAlmostEqual(self.percent_mod.apply(50), 60)  # 50 * 1.2 = 60

    def test_apply_multiplier(self):
        self.assertEqual(self.mult_mod.apply(40), 60)  # 40 * 1.5 = 60

    def test_apply_no_type_match(self):
        mod = Modifier(name="Unknown", value=5, modifier_type=None)
        self.assertEqual(mod.apply(10), 10)

    # --- Test tick() ---
    def test_tick_decrements_duration(self):
        expired = self.temp_mod.tick()
        self.assertFalse(expired)
        self.assertEqual(self.temp_mod.duration, 1)

    def test_tick_expiration(self):
        self.temp_mod.tick()  # duration 2 -> 1
        expired = self.temp_mod.tick()  # duration 1 -> 0
        self.assertTrue(expired)

    def test_tick_no_duration(self):
        self.assertFalse(self.flat_mod.tick())

    # --- Test equality ---
    def test_equality_true(self):
        mod_copy = Modifier(
            name="Flat Boost",
            value=10,
            modifier_type=ModifierType.FLAT
        )
        self.assertEqual(self.flat_mod, mod_copy)

    def test_equality_false(self):
        mod_diff = Modifier(
            name="Flat Boost",
            value=5,
            modifier_type=ModifierType.FLAT
        )
        self.assertNotEqual(self.flat_mod, mod_diff)

    # --- Test serialization ---
    def test_serialize_deserialize(self):
        serialized = self.percent_mod.serialize()
        deserialized = Modifier.deserialize(serialized)
        self.assertEqual(self.percent_mod, deserialized)

    # --- Test __repr__ ---
    def test_repr_flat(self):
        self.assertEqual(repr(self.flat_mod), "+10")

    def test_repr_percentage(self):
        self.assertEqual(repr(self.percent_mod), "+20%")

    def test_repr_multiplier(self):
        self.assertEqual(repr(self.mult_mod), "x1.5")


if __name__ == "__main__":
    unittest.main()
