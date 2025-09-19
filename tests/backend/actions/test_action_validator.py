import unittest
from src.backend.actions import ActionValidator
from src.backend.board import Board
from src.backend.entities.pieces import (
    Bishop, King, Knight, Pawn, Rook, Queen
)


class TestActionValidator(unittest.TestCase):
    def setUp(self):
        self.board = Board(8, 8)
        self.action_validator = ActionValidator(self.board)


if __name__ == "__main__":
    unittest.main()
