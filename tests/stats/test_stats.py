import unittest

from src.stats import Modifier, ModifierType, Stat, Stats


class TestStats(unittest.TestCase):
    def test_creation(self):
        stats = Stats()
        self.assertEqual(stats.serialize(), {})

    def test_add(self):
        stats = Stats()

        stats["stat1"] = Stat("Stat 1", 10)

        self.assertDictEqual(
            stats.serialize(),
            {
                "stat1": {
                    "name": "Stat 1",
                    "base_value": 10,
                    "min_value": 0,
                    "max_value": float('inf'),
                    "modifiers": {}
                }
            }
        )

    def test_add_multiple(self):
        stats = Stats()

        stats["stat1"] = Stat("Stat 1", 10)
        stats["stat2"] = Stat("Stat 2", 10)
        stats["stat3"] = Stat("Stat 3", 10)

        self.assertDictEqual(
            stats.serialize(),
            {
                "stat1": {
                    "name": "Stat 1",
                    "base_value": 10,
                    "min_value": 0,
                    "max_value": float('inf'),
                    "modifiers": {}
                },
                "stat2": {
                    "name": "Stat 2",
                    "base_value": 10,
                    "min_value": 0,
                    "max_value": float('inf'),
                    "modifiers": {}
                },
                "stat3": {
                    "name": "Stat 3",
                    "base_value": 10,
                    "min_value": 0,
                    "max_value": float('inf'),
                    "modifiers": {}
                }
            }
        )

    def test_add_modifier(self):
        stats = Stats()

        stats["stat1"] = Stat("Stat 1", 10)

        modifier = Modifier("mod1", 10, ModifierType.FLAT)
        stats["stat1"].add_modifier(modifier)

        self.assertDictEqual(
            stats.serialize(),
            {
                "stat1": {
                    "name": "Stat 1",
                    "base_value": 10,
                    "min_value": 0,
                    "max_value": float('inf'),
                    "modifiers": {
                        "mod1": {
                            "name": "mod1",
                            "value": 10,
                            "modifier_type": "flat",
                            "source": "global",
                            "duration": None
                        }
                    }
                }
            }
        )


if __name__ == "__main__":
    unittest.main()
