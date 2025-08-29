import unittest

from src.board import Board
from src.constants import BOARD_ROW_SIZE, BOARD_COL_SIZE
from src.pieces import Pawn


class TestBoard(unittest.TestCase):
    def test_creation(self):
        board = Board()
        self.assertEqual(board.size, (BOARD_ROW_SIZE, BOARD_COL_SIZE))

    def test_add_piece(self):
        board = Board()
        piece = Pawn()
        board.add_entity((0, 0), piece)
        self.assertEqual(board.get_entity((0, 0)), piece)

    def test_add_pieces(self):
        board = Board()
        pawn1 = Pawn()
        pawn2 = Pawn()
        board.add_entity((0, 0), pawn1)
        board.add_entity((0, 1), pawn2)
        self.assertEqual(board.get_entity((0, 0)), pawn1)
        self.assertEqual(board.get_entity((0, 1)), pawn2)

    def test_remove_piece(self):
        board = Board()
        pawn1 = Pawn()
        pawn2 = Pawn()
        board.add_entity((0, 0), pawn1)
        board.add_entity((0, 1), pawn2)
        board.remove_entity((0, 0))
        board.remove_entity((0, 1))
        self.assertEqual(board.get_entity((0, 0)), None)
        self.assertEqual(board.get_entity((0, 1)), None)

    def test_move_piece(self):
        board = Board()
        pawn = Pawn()
        board.add_entity((0, 0), pawn)
        board.move_entity((0, 0), (0, 1))
        self.assertEqual(board.get_entity((0, 1)), pawn)
        self.assertEqual(board.get_entity((0, 0)), None)


if __name__ == "__main__":
    unittest.main()
