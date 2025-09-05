import unittest
from src.backend.stats import Resource, Modifier, ModifierType


class TestResource(unittest.TestCase):
    def setUp(self):
        self.resource = Resource(
            name="Mana",
            base_value=100,
            current=50
        )

        self.temp_mod = Modifier(
            name="Temp Boost",
            value=20,
            modifier_type=ModifierType.FLAT,
            duration=2,
            source="potion"
        )

    # --- Initialization ---
    def test_initial_values(self):
        r = Resource(name="Health", base_value=150)
        self.assertEqual(r.value, 150)
        self.assertEqual(r.current, 150)

    def test_current_clamped_to_max(self):
        self.resource._current = 200
        self.assertEqual(self.resource.current, self.resource.max)

    # --- Take / Give ---
    def test_take_resource(self):
        self.resource.take(20)
        self.assertEqual(self.resource.current, 30)

    def test_give_resource(self):
        self.resource.give(30)
        self.assertEqual(self.resource.current, 80)

    def test_take_below_zero(self):
        self.resource.take(100)
        self.assertEqual(self.resource.current, 0)
        self.assertTrue(self.resource.is_depleted())

    def test_give_above_max(self):
        self.resource.give(100)
        self.assertEqual(self.resource.current, self.resource.max)

    # --- Refill ---
    def test_refill(self):
        self.resource.take(30)
        self.resource.refill()
        self.assertEqual(self.resource.current, self.resource.max)

    # --- Tick behavior ---
    def test_tick_modifiers(self):
        self.resource.add_modifier(self.temp_mod)
        self.assertEqual(self.resource.value, 120)

        # First tick, duration 2 -> 1, modifier still active
        expired = self.resource.tick()
        self.assertEqual(expired, [])
        self.assertEqual(self.resource.value, 120)
        self.assertEqual(self.temp_mod.duration, 1)

        # Second tick, modifier expires
        expired = self.resource.tick()
        self.assertEqual(len(expired), 1)
        self.assertEqual(expired[0].name, "Temp Boost")
        self.assertEqual(self.resource.value, 100)

        # Tick when no modifiers left
        expired = self.resource.tick()
        self.assertEqual(expired, [])

    # --- Serialization ---
    def test_serialize_deserialize(self):
        self.resource.add_modifier(self.temp_mod)
        self.resource.take(30)
        data = self.resource.serialize()
        new_res = Resource.deserialize(data)
        self.assertEqual(new_res.base_value, self.resource.base_value)
        self.assertEqual(new_res.current, self.resource.current)
        self.assertEqual(
            len(new_res._modifiers), len(self.resource._modifiers)
        )
        self.assertEqual(new_res._modifiers[0].name, "Temp Boost")


if __name__ == "__main__":
    unittest.main()
