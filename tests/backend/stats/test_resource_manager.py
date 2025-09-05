import unittest
from src.backend.stats import Resource, Modifier, ModifierType
from src.backend.stats import ResourceManager


class TestResourceManager(unittest.TestCase):
    def setUp(self):
        # Resources
        self.mana = Resource(name="Mana", base_value=100)
        self.health = Resource(name="Health", base_value=200)

        # Temporary modifiers
        self.temp_mod = Modifier(
            name="Temp Boost",
            value=20,
            modifier_type=ModifierType.FLAT,
            duration=2
        )

        # Resource manager
        self.manager = ResourceManager()
        self.manager.add_resource(self.mana)
        self.manager.add_resource(self.health)

    # --- Accessors ---
    def test_get_resource(self):
        self.assertEqual(self.manager.get_resource("Mana"), self.mana)
        self.assertEqual(self.manager.get_resource("health"), self.health)

    def test_contains_resource(self):
        self.assertTrue(self.manager.contains_resource("mana"))
        self.assertTrue(self.manager.contains_resource("Health"))
        self.assertFalse(self.manager.contains_resource("Stamina"))

    def test_item_access(self):
        self.assertEqual(self.manager["mana"], self.mana)
        self.assertIn("Health", self.manager)

    # --- Tick ---
    def test_tick_modifiers(self):
        self.mana.add_modifier(self.temp_mod)
        expired1 = self.manager.tick()
        # Duration goes from 2 -> 1, so no expiration yet
        self.assertEqual(expired1, {})
        expired2 = self.manager.tick()
        # Duration goes from 1 -> 0, modifier should expire
        self.assertIn("mana", expired2)
        self.assertEqual(expired2["mana"][0], self.temp_mod)
        # After expiration, the modifier should be removed
        self.assertIsNone(self.mana.get_modifier("Temp Boost"))

    # --- Serialization ---
    def test_serialize_deserialize(self):
        self.mana.add_modifier(self.temp_mod)
        data = self.manager.serialize()
        new_manager = ResourceManager.deserialize(data)
        # Resources exist
        self.assertIn("mana", new_manager)
        self.assertIn("health", new_manager)
        # Modifier exists in deserialized resource
        mana_res = new_manager.get_resource("mana")
        mod = mana_res.get_modifier("Temp Boost")
        self.assertIsNotNone(mod)
        self.assertEqual(mod.value, 20)
        self.assertEqual(mod.duration, 2)


if __name__ == "__main__":
    unittest.main()
