import unittest

from src.entities.pieces import Piece, Pawn, Bishop, Knight, Rook, Queen, King
from src.constants import (
    PAWN_DAMAGE, PAWN_HEALTH, PAWN_NAME, PAWN_RANGE, PAWN_VALUE,
    BISHOP_DAMAGE, BISHOP_HEALTH, BISHOP_NAME, BISHOP_RANGE, BISHOP_VALUE,
    KNIGHT_DAMAGE, KNIGHT_HEALTH, KNIGHT_NAME, KNIGHT_RANGE, KNIGHT_VALUE,
    ROOK_DAMAGE, ROOK_HEALTH, ROOK_NAME, ROOK_RANGE, ROOK_VALUE,
    QUEEN_DAMAGE, QUEEN_HEALTH, QUEEN_NAME, QUEEN_RANGE, QUEEN_VALUE,
    KING_DAMAGE, KING_HEALTH, KING_NAME, KING_RANGE, KING_VALUE,
)


class TestPieces(unittest.TestCase):
    def check_piece(self, piece: Piece, name, value, health, damage, range_):
        """Helper to check the stats of a piece."""
        self.assertEqual(piece.name, name)
        self.assertIn("value", piece.stats)
        self.assertIn("max_health", piece.stats)
        self.assertIn("damage", piece.stats)
        self.assertIn("range", piece.stats)

        self.assertEqual(piece.stats["value"].value, value)
        self.assertEqual(piece.stats["max_health"].value, health)
        self.assertEqual(piece.stats["damage"].value, damage)
        self.assertEqual(piece.stats["range"].value, range_)

    def test_pawn(self):
        self.check_piece(
            Pawn(),
            PAWN_NAME,
            PAWN_VALUE,
            PAWN_HEALTH,
            PAWN_DAMAGE,
            PAWN_RANGE
        )

    def test_bishop(self):
        self.check_piece(
            Bishop(),
            BISHOP_NAME,
            BISHOP_VALUE,
            BISHOP_HEALTH,
            BISHOP_DAMAGE,
            BISHOP_RANGE
        )

    def test_knight(self):
        self.check_piece(
            Knight(),
            KNIGHT_NAME,
            KNIGHT_VALUE,
            KNIGHT_HEALTH,
            KNIGHT_DAMAGE,
            KNIGHT_RANGE
        )

    def test_rook(self):
        self.check_piece(
            Rook(),
            ROOK_NAME,
            ROOK_VALUE,
            ROOK_HEALTH,
            ROOK_DAMAGE,
            ROOK_RANGE
        )

    def test_queen(self):
        self.check_piece(
            Queen(),
            QUEEN_NAME,
            QUEEN_VALUE,
            QUEEN_HEALTH,
            QUEEN_DAMAGE,
            QUEEN_RANGE
        )

    def test_king(self):
        self.check_piece(
            King(),
            KING_NAME,
            KING_VALUE,
            KING_HEALTH,
            KING_DAMAGE,
            KING_RANGE
        )


if __name__ == "__main__":
    unittest.main()
