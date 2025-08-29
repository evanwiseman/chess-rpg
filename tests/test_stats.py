import unittest

from src.modifier import Modifier, ModifierType
from src.stats import Stats


class TestStats(unittest.TestCase):
    def test_creation(self):
        stats = Stats()
        self.assertEqual(stats.to_dict(), {})

    def test_add(self):
        stats = Stats()

        stats.add("stat1", 10)

        self.assertDictEqual(
            stats.to_dict(),
            {
                "stat1": {
                    "name": "stat1",
                    "base_value": 10,
                    "min_value": 0,
                    "max_value": float('inf'),
                    "modifiers": {}
                }
            }
        )

    def test_add_multiple(self):
        stats = Stats()

        stat1 = stats.add("stat1", 10)
        stat2 = stats.add("stat2", 10)
        stat3 = stats.add("stat3", 10)

        self.assertDictEqual(
            stats.to_dict(),
            {
                "stat1": {
                    "name": "stat1",
                    "base_value": 10,
                    "min_value": 0,
                    "max_value": float('inf'),
                    "modifiers": {}
                },
                "stat2": {
                    "name": "stat2",
                    "base_value": 10,
                    "min_value": 0,
                    "max_value": float('inf'),
                    "modifiers": {}
                },
                "stat3": {
                    "name": "stat3",
                    "base_value": 10,
                    "min_value": 0,
                    "max_value": float('inf'),
                    "modifiers": {}
                }
            }
        )
        self.assertEqual(stat1, stats["stat1"])
        self.assertEqual(stat2, stats["stat2"])
        self.assertEqual(stat3, stats["stat3"])

    def test_add_modifier(self):
        stats = Stats()

        stats.add("stat1", 10)

        modifier = Modifier("mod1", 10, ModifierType.FLAT)
        stats["stat1"].add_modifier(modifier)

        self.assertDictEqual(
            stats.to_dict(),
            {
                "stat1": {
                    "name": "stat1",
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
