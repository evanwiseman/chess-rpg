import unittest
from src.backend.stats import StatsManager, Stat, Modifier, ModifierType


class TestStatsManager(unittest.TestCase):
    def setUp(self):
        self.manager = StatsManager()
        self.health = Stat(name="Health", base_value=100)
        self.mana = Stat(name="Mana", base_value=50)

        self.temp_mod = Modifier(
            name="Temp Boost",
            value=10,
            modifier_type=ModifierType.FLAT,
            duration=2,
            source="potion"
        )

    # --- Adding and retrieving stats ---
    def test_add_and_get_stat(self):
        self.manager.add_stat(self.health)
        stat = self.manager.get_stat("Health")
        self.assertEqual(stat, self.health)

    def test_add_via_add_method(self):
        self.manager.add("Stamina", 75)
        self.assertTrue(self.manager.contains_stat("Stamina"))
        stat = self.manager.get_stat("Stamina")
        self.assertEqual(stat.base_value, 75)

    # --- contains / __contains__ ---
    def test_contains_stat(self):
        self.manager.add_stat(self.health)
        self.assertTrue(self.manager.contains_stat("Health"))
        self.assertTrue("health" in self.manager)
        self.assertFalse(self.manager.contains_stat("Mana"))
        self.assertFalse("mana" in self.manager)

    # --- dict-like access ---
    def test_getitem(self):
        self.manager.add_stat(self.health)
        self.assertEqual(self.manager["Health"], self.health)
        with self.assertRaises(KeyError):
            _ = self.manager["Nonexistent"]

    # --- tick functionality ---
    def test_tick_modifiers(self):
        self.health.add_modifier(self.temp_mod)
        self.manager.add_stat(self.health)
        expired = self.manager.tick()
        # duration 2 -> 1, modifier still active
        self.assertEqual(expired, {})
        self.assertEqual(self.health.value, 110)
        self.assertEqual(self.temp_mod.duration, 1)

        # tick again, modifier expires
        expired = self.manager.tick()
        self.assertIn("health", expired)
        self.assertEqual(expired["health"][0].name, "Temp Boost")
        self.assertEqual(self.health.value, 100)

    # --- serialization / deserialization ---
    def test_serialize_deserialize(self):
        self.manager.add_stat(self.health)
        self.manager.add_stat(self.mana)
        data = self.manager.serialize()
        new_mgr = StatsManager.deserialize(data)
        self.assertTrue("health" in new_mgr)
        self.assertTrue("mana" in new_mgr)
        self.assertEqual(new_mgr.get_stat("Health").base_value, 100)
        self.assertEqual(new_mgr.get_stat("Mana").base_value, 50)


if __name__ == "__main__":
    unittest.main()
