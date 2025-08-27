import unittest

from src.stats import Stats, MovementType


class TestStats(unittest.TestCase):
    def test_zero(self):
        stats = Stats(0, 0, 0, {MovementType.FORWARD})
        self.assertEqual(stats.hp, 0)
        self.assertEqual(stats.damage, 0)
        self.assertEqual(stats.movement_range, 0)
        self.assertSetEqual(stats.movement_types, {MovementType.FORWARD})

    def test_negative(self):
        stats = Stats(-1, -1, -1, {MovementType.FORWARD})
        self.assertEqual(stats.hp, 0)
        self.assertEqual(stats.damage, 0)
        self.assertEqual(stats.movement_range, 0)
        self.assertSetEqual(stats.movement_types, {MovementType.FORWARD})

    def test_positive(self):
        stats = Stats(10, 10, 10, {MovementType.FORWARD})
        self.assertEqual(stats.hp, 10)
        self.assertEqual(stats.damage, 10)
        self.assertEqual(stats.movement_range, 10)
        self.assertSetEqual(stats.movement_types, {MovementType.FORWARD})

    def test_unlimited_range(self):
        stats = Stats(10, 10, None, {MovementType.FORWARD})
        self.assertEqual(stats.hp, 10)
        self.assertEqual(stats.damage, 10)
        self.assertEqual(stats.movement_range, None)
        self.assertSetEqual(stats.movement_types, {MovementType.FORWARD})

    def test_multiple_movement_types(self):
        stats = Stats(10, 10, 1, {MovementType.FORWARD, MovementType.BACKWARD})
        self.assertEqual(stats.hp, 10)
        self.assertEqual(stats.damage, 10)
        self.assertEqual(stats.movement_range, 1)
        self.assertSetEqual(
            stats.movement_types,
            {MovementType.FORWARD, MovementType.BACKWARD}
        )


if __name__ == "__main__":
    unittest.main()
