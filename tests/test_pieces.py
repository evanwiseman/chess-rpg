import unittest

from src import Pawn, Bishop, Knight, Rook, Queen, King
from src import (
    PAWN_STATS, BISHOP_STATS, KNIGHT_STATS, ROOK_STATS, QUEEN_STATS, KING_STATS
)
from src import MovementType


class TestPieces(unittest.TestCase):
    def test_pawn(self):
        pawn = Pawn()
        self.assertEqual(pawn.stats, PAWN_STATS)

    def test_bishop(self):
        bishop = Bishop()
        self.assertEqual(bishop.stats, BISHOP_STATS)

    def test_knight(self):
        knight = Knight()
        self.assertEqual(knight.stats, KNIGHT_STATS)

    def test_rook(self):
        rook = Rook()
        self.assertEqual(rook.stats, ROOK_STATS)

    def test_queen(self):
        queen = Queen()
        self.assertEqual(queen.stats, QUEEN_STATS)

    def test_king(self):
        king = King()
        self.assertEqual(king.stats, KING_STATS)

    def test_modified_hp(self):
        pawn = Pawn()
        pawn.stats.hp += 10
        self.assertNotEqual(pawn.stats, PAWN_STATS)

    def test_modified_damage(self):
        pawn = Pawn()
        pawn.stats.damage += 10
        self.assertNotEqual(pawn.stats, PAWN_STATS)

    def test_modified_movement_range(self):
        pawn = Pawn()
        pawn.stats.movement_range += 1
        self.assertNotEqual(pawn.stats, PAWN_STATS)

    def test_modified_movement_types(self):
        pawn = Pawn()
        pawn.stats.movement_types.add(MovementType.BACKWARD)
        self.assertNotEqual(pawn.stats, PAWN_STATS)

    def test_modified_all(self):
        pawn = Pawn()
        pawn.stats.hp += 10
        pawn.stats.damage += 10
        pawn.stats.movement_range += 1
        pawn.stats.movement_types.add(MovementType.BACKWARD)
        self.assertNotEqual(pawn.stats.hp, PAWN_STATS.hp)
        self.assertNotEqual(pawn.stats.damage, PAWN_STATS.damage)
        self.assertNotEqual(
            pawn.stats.movement_range,
            PAWN_STATS.movement_range
        )
        self.assertNotEqual(
            pawn.stats.movement_types,
            PAWN_STATS.movement_types
        )
        self.assertNotEqual(pawn.stats, PAWN_STATS)


if __name__ == "__main__":
    unittest.main()
