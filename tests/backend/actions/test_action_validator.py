import unittest
from src.backend.actions import ActionValidator, MoveAction
from src.backend.board import Board
from src.backend.entities.pieces import (
    Bishop, King, Knight, Rook, Queen
)


class TestActionValidator(unittest.TestCase):
    def setUp(self):
        self.board = Board(8, 8)
        self.action_validator = ActionValidator(self.board)

    def test_bishop_moves(self):
        bishop = Bishop()
        self.board.place_piece(bishop, (4, 4))
        valid_moves = self.action_validator.get_valid_moves(bishop)

        self.assertIn(
            MoveAction(bishop, (0, 0)),
            valid_moves
        )
        self.assertIn(
            MoveAction(bishop, (7, 7)),
            valid_moves
        )
        self.assertIn(
            MoveAction(bishop, (1, 7)),
            valid_moves
        )
        self.assertIn(
            MoveAction(bishop, (7, 1)),
            valid_moves
        )

    def test_king_moves(self):
        king = King()
        self.board.place_piece(king, (4, 4))
        valid_moves = self.action_validator.get_valid_moves(king)

        self.assertEqual(len(valid_moves), 8)
        self.assertIn(
            MoveAction(king, (3, 3)),
            valid_moves
        )
        self.assertIn(
            MoveAction(king, (3, 4)),
            valid_moves
        )
        self.assertIn(
            MoveAction(king, (3, 5)),
            valid_moves
        )
        self.assertIn(
            MoveAction(king, (4, 3)),
            valid_moves
        )
        self.assertIn(
            MoveAction(king, (4, 5)),
            valid_moves
        )
        self.assertIn(
            MoveAction(king, (5, 3)),
            valid_moves
        )
        self.assertIn(
            MoveAction(king, (5, 4)),
            valid_moves
        )
        self.assertIn(
            MoveAction(king, (5, 5)),
            valid_moves
        )

    def test_knight_moves(self):
        knight = Knight()
        self.board.place_piece(knight, (4, 4))
        valid_moves = self.action_validator.get_valid_moves(knight)

        self.assertEqual(len(valid_moves), 8)
        self.assertIn(
            MoveAction(knight, (2, 3)),
            valid_moves
        )
        self.assertIn(
            MoveAction(knight, (3, 2)),
            valid_moves
        )
        self.assertIn(
            MoveAction(knight, (5, 2)),
            valid_moves
        )
        self.assertIn(
            MoveAction(knight, (6, 3)),
            valid_moves
        )
        self.assertIn(
            MoveAction(knight, (6, 5)),
            valid_moves
        )
        self.assertIn(
            MoveAction(knight, (5, 6)),
            valid_moves
        )
        self.assertIn(
            MoveAction(knight, (3, 6)),
            valid_moves
        )
        self.assertIn(
            MoveAction(knight, (2, 5)),
            valid_moves
        )

    def test_rook_moves(self):
        rook = Rook()
        self.board.place_piece(rook, (4, 4))
        valid_moves = self.action_validator.get_valid_moves(rook)

        self.assertEqual(len(valid_moves), 14)
        self.assertIn(
            MoveAction(rook, (4, 7)),
            valid_moves
        )
        self.assertIn(
            MoveAction(rook, (4, 0)),
            valid_moves
        )
        self.assertIn(
            MoveAction(rook, (7, 4)),
            valid_moves
        )
        self.assertIn(
            MoveAction(rook, (0, 4)),
            valid_moves
        )

    def test_queen_moves(self):
        queen = Queen()
        self.board.place_piece(queen, (4, 4))
        valid_moves = self.action_validator.get_valid_moves(queen)

        self.assertEqual(len(valid_moves), 27)
        self.assertIn(
            MoveAction(queen, (0, 0)),
            valid_moves
        )
        self.assertIn(
            MoveAction(queen, (7, 7)),
            valid_moves
        )
        self.assertIn(
            MoveAction(queen, (1, 7)),
            valid_moves
        )
        self.assertIn(
            MoveAction(queen, (7, 1)),
            valid_moves
        )
        self.assertIn(
            MoveAction(queen, (4, 7)),
            valid_moves
        )
        self.assertIn(
            MoveAction(queen, (4, 0)),
            valid_moves
        )
        self.assertIn(
            MoveAction(queen, (7, 4)),
            valid_moves
        )
        self.assertIn(
            MoveAction(queen, (0, 4)),
            valid_moves
        )


if __name__ == "__main__":
    unittest.main()
