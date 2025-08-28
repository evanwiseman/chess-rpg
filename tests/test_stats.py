import unittest

from src.stats import ModifierType, Modifier, Stat, Stats


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


class TestStat(unittest.TestCase):
    def test_creation(self):
        stat = Stat("stat", 10)
        self.assertEqual(stat.name, "stat")
        self.assertEqual(stat.base_value, 10)
        self.assertEqual(stat.value, 10)
        self.assertEqual(stat.min_value, 0)
        self.assertEqual(stat.max_value, float('inf'))
        self.assertDictEqual(stat._modifiers, {})

    def test_add_flat(self):
        stat = Stat("stat", 10)
        self.assertEqual(stat._cache_dirty, True)
        self.assertEqual(stat.value, 10)
        self.assertEqual(stat._cache_dirty, False)
        stat.add_modifier(Modifier("modifier", 10, ModifierType.FLAT, "test"))
        self.assertEqual(stat.base_value, 10)
        self.assertEqual(stat._cache_dirty, True)
        self.assertEqual(stat.value, 20)
        self.assertEqual(stat._cache_dirty, False)

    def test_remove_flat(self):
        stat = Stat("stat", 10)
        stat.add_modifier(Modifier("modifier", 10, ModifierType.FLAT, "test"))
        stat.remove_modifier("modifier")
        self.assertEqual(stat._cache_dirty, True)
        self.assertEqual(stat.value, 10)
        self.assertEqual(stat._cache_dirty, False)

    def test_add_multiple_flat(self):
        stat = Stat("stat", 10)
        stat.add_modifier(Modifier("mod1", 10, ModifierType.FLAT, "test"))
        stat.add_modifier(Modifier("mod2", 10, ModifierType.FLAT, "test"))
        self.assertEqual(stat.value, 30)

    def test_remove_multiple_flat(self):
        stat = Stat("stat", 10)
        stat.add_modifier(Modifier("mod1", 10, ModifierType.FLAT, "test"))
        stat.add_modifier(Modifier("mod2", 10, ModifierType.FLAT, "test"))
        stat.remove_modifier("mod1")
        stat.remove_modifier("mod2")
        self.assertEqual(stat.value, 10)

    def test_add_multiple_all(self):
        stat = Stat("stat", 10)
        stat.add_modifier(
            Modifier("mod1", 10, ModifierType.FLAT, "test")
        )
        stat.add_modifier(
            Modifier("mod2", 100, ModifierType.PERCENTAGE, "test")
        )
        stat.add_modifier(
            Modifier("mod3", 2, ModifierType.MULTIPLIER, "test")
        )
        self.assertEqual(stat.value, 80)

    def test_remove_multiple_all(self):
        stat = Stat("stat", 10)
        stat.add_modifier(
            Modifier("mod1", 10, ModifierType.FLAT, "test")
        )
        stat.add_modifier(
            Modifier("mod2", 100, ModifierType.PERCENTAGE, "test")
        )
        stat.add_modifier(
            Modifier("mod3", 2, ModifierType.MULTIPLIER, "test")
        )
        stat.remove_modifier("mod3")
        stat.remove_modifier("mod2")
        stat.remove_modifier("mod1")
        self.assertEqual(stat.value, 10)

    def test_add_multiple_source(self):
        stat = Stat("stat", 10)
        stat.add_modifier(
            Modifier("mod1", 10, ModifierType.FLAT, "test1")
        )
        stat.add_modifier(
            Modifier("mod2", 10, ModifierType.FLAT, "test2")
        )
        self.assertEqual(stat.value, 30)

    def test_remove_source(self):
        stat = Stat("stat", 10)
        stat.add_modifier(Modifier("mod1", 10, ModifierType.FLAT, "test"))
        stat.remove_modifiers_by_source("test")
        self.assertEqual(stat.value, 10)
        self.assertDictEqual(stat._modifiers, {})
        self.assertDictEqual(stat._sources, {})

    def test_update_durations(self):
        stat = Stat("stat", 10)
        stat.add_modifier(Modifier("mod1", 10, ModifierType.FLAT, "test", 1))
        expired = stat.update_durations()
        self.assertEqual(len(expired), 1)
        self.assertEqual(
            expired[0],
            Modifier("mod1", 10, ModifierType.FLAT, "test", 0)
        )


class TestStats(unittest.TestCase):
    def test_creation(self):
        stats = Stats()
        self.assertEqual(stats.to_dict(), {})

    def test_add(self):
        stats = Stats()
        stats.add("stat1", 10)

    def test_add_multiple(self):
        stats = Stats()
        stats.add("stat1", 10)
        stats.add("stat2", 10)
        stats.add("stat3", 10)
        self.assertDictEqual(
            stats.to_dict(),
            {
                "stat1": {
                    "name": "stat1",
                    "base_value": 10,
                    "min_value": 0,
                    "max_value": float('inf'),
                    "modifiers": []
                },
                "stat2": {
                    "name": "stat2",
                    "base_value": 10,
                    "min_value": 0,
                    "max_value": float('inf'),
                    "modifiers": []
                },
                "stat3": {
                    "name": "stat3",
                    "base_value": 10,
                    "min_value": 0,
                    "max_value": float('inf'),
                    "modifiers": []
                }
            }
        )

    def test_add_modifier(self):
        stats = Stats()
        stats.add("stat1", 10)
        stats["stat1"].add_modifier(Modifier("mod1", 10, ModifierType.FLAT))

        equiv_stat = Stat("stat1", 10)
        equiv_stat.add_modifier(Modifier("mod1", 10, ModifierType.FLAT))


if __name__ == "__main__":
    unittest.main()
