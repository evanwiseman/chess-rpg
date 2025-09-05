import unittest
from src.backend.stats import Stat, Modifier, ModifierType


class TestStat(unittest.TestCase):
    def setUp(self):
        self.stat = Stat(
            name="Health",
            base_value=100,
            min_value=0,
            max_value=200
        )

        self.flat_mod = Modifier(
            name="Flat Boost",
            value=10,
            modifier_type=ModifierType.FLAT,
            source="potion"
        )
        self.percent_mod = Modifier(
            name="Percent Boost",
            value=20,
            modifier_type=ModifierType.PERCENTAGE,
            source="aura"
        )
        self.mult_mod = Modifier(
            name="Multiplier Boost",
            value=2,
            modifier_type=ModifierType.MULTIPLIER,
            source="buff"
        )
        self.temp_mod = Modifier(
            name="Temporary Boost",
            value=5,
            modifier_type=ModifierType.FLAT,
            duration=2,
            source="potion"
        )

    # --- Base behavior ---
    def test_base_value_no_modifiers(self):
        self.assertEqual(self.stat.value, 100)

    # --- Adding modifiers ---
    def test_add_flat_modifier(self):
        self.stat.add_modifier(self.flat_mod)
        self.assertEqual(self.stat.value, 110)

    def test_add_percentage_modifier(self):
        self.stat.add_modifier(self.percent_mod)
        # 100 * 1.2 = 120
        self.assertEqual(self.stat.value, 120)

    def test_add_multiplier_modifier(self):
        self.stat.add_modifier(self.mult_mod)
        # 100 * 2 = 200
        self.assertEqual(self.stat.value, 200)

    def test_combined_modifiers_order(self):
        # Apply flat first: 100 + 10 = 110
        # Apply percentage: 110 * 1.2 = 132
        # Apply multiplier: 132 * 2 = 264 -> capped at max (200)
        self.stat.add_modifier(self.flat_mod)
        self.stat.add_modifier(self.percent_mod)
        self.stat.add_modifier(self.mult_mod)
        self.assertEqual(self.stat.value, 200)

    # --- Removing modifiers ---
    def test_remove_single_modifier(self):
        self.stat.add_modifier(self.flat_mod)
        self.stat.remove_modifier(self.flat_mod)
        self.assertEqual(self.stat.value, 100)

    def test_remove_modifiers_by_source(self):
        self.stat.add_modifier(self.flat_mod)
        self.stat.add_modifier(self.percent_mod)
        self.stat.remove_modifiers_by_source("potion")
        self.assertEqual(len(self.stat._modifiers), 1)
        self.assertEqual(self.stat.value, 120)

    def test_remove_modifiers_by_source_none(self):
        self.stat.add_modifier(self.percent_mod)
        removed = self.stat.remove_modifiers_by_source("potion")
        self.assertFalse(removed)
        self.assertEqual(len(self.stat._modifiers), 1)

    # --- Tick behavior ---
    def test_tick_modifiers(self):
        self.stat.add_modifier(self.temp_mod)
        self.assertEqual(self.stat.value, 105)

        # Tick once, duration goes 2 -> 1, modifier still active
        expired = self.stat.tick()
        self.assertEqual(expired, [])
        self.assertEqual(self.stat.value, 105)
        self.assertEqual(self.temp_mod.duration, 1)

        # Tick again, duration goes 1 -> 0, modifier expires
        expired = self.stat.tick()
        self.assertEqual(len(expired), 1)
        self.assertEqual(expired[0].name, "Temporary Boost")
        self.assertEqual(self.stat.value, 100)  # modifier removed

        # Tick with no active temporary modifiers
        expired = self.stat.tick()
        self.assertEqual(expired, [])

    # --- Cache behavior ---
    def test_cache_dirty_flag(self):
        self.assertTrue(self.stat._cache_dirty)  # initial
        _ = self.stat.value  # calculate once
        self.assertFalse(self.stat._cache_dirty)
        self.stat.add_modifier(self.flat_mod)  # should dirty cache
        self.assertTrue(self.stat._cache_dirty)

    # --- Serialization ---
    def test_serialize_deserialize(self):
        self.stat.add_modifier(self.flat_mod)
        self.stat.add_modifier(self.percent_mod)
        data = self.stat.serialize()
        new_stat = Stat.deserialize(data)
        self.assertEqual(self.stat, new_stat)


if __name__ == "__main__":
    unittest.main()
