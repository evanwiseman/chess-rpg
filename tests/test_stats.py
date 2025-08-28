import unittest

from src.modifier import Modifier, ModifierType
from src.stat import Stat
from src.stats import Stats


class TestStats(unittest.TestCase):
    def test_creation(self):
        stats = Stats()
        self.assertEqual(stats.to_dict(), {})

    def test_add(self):
        stats = Stats()

        stat = Stat("stat1", 10)
        stats.add(stat)

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

        stat1 = Stat("stat1", 10)
        stats.add(stat1)

        stat2 = Stat("stat2", 10)
        stats.add(stat2)

        stat3 = Stat("stat3", 10)
        stats.add(stat3)

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

    def test_add_modifier(self):
        stats = Stats()

        stat = Stat("stat1", 10)
        stats.add(stat)

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
