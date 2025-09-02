import unittest

from src.game import Board
from src.constants import BOARD_ROW_SIZE, BOARD_COL_SIZE
from src.entities.pieces import Pawn


class TestBoard(unittest.TestCase):
    def test_creation(self):
        board = Board()
        self.assertEqual(board.size, (BOARD_ROW_SIZE, BOARD_COL_SIZE))

    def test_add_entity(self):
        board = Board()
        piece = Pawn()
        board.add_entity((0, 0), piece)
        self.assertEqual(board.get_entity_at((0, 0)), piece)
        self.assertEqual(board.get_entity_by_id(piece.id), piece)
        self.assertEqual(board.get_entity_location(piece), (0, 0))

    def test_add_entity_multi(self):
        board = Board()
        pawn1 = Pawn()
        pawn2 = Pawn()
        board.add_entity((0, 0), pawn1)
        board.add_entity((0, 1), pawn2)
        self.assertEqual(board.get_entity_at((0, 0)), pawn1)
        self.assertEqual(board.get_entity_by_id(pawn1.id), pawn1)
        self.assertEqual(board.get_entity_location(pawn1), (0, 0))
        self.assertEqual(board.get_entity_at((0, 1)), pawn2)
        self.assertEqual(board.get_entity_by_id(pawn2.id), pawn2)
        self.assertEqual(board.get_entity_location(pawn2), (0, 1))

    def test_remove_entity_at(self):
        board = Board()
        pawn1 = Pawn()
        pawn2 = Pawn()
        board.add_entity((0, 0), pawn1)
        board.add_entity((0, 1), pawn2)
        board.remove_entity_at((0, 0))
        board.remove_entity_at((0, 1))
        self.assertEqual(board.get_entity_at((0, 0)), None)
        self.assertEqual(board.get_entity_by_id(pawn1.id), None)
        self.assertEqual(board.get_entity_location(pawn1), (-1, -1))
        self.assertEqual(board.get_entity_at((0, 1)), None)
        self.assertEqual(board.get_entity_by_id(pawn2.id), None)
        self.assertEqual(board.get_entity_location(pawn2), (-1, -1))

    def test_remove_entity(self):
        """
        Tests both remove_entity and remove_entity_by_id
        """
        board = Board()
        pawn1 = Pawn()
        pawn2 = Pawn()
        board.add_entity((0, 0), pawn1)
        board.add_entity((0, 1), pawn2)
        board.remove_entity(pawn1)
        board.remove_entity(pawn2)
        self.assertEqual(board.get_entity_at((0, 0)), None)
        self.assertEqual(board.get_entity_by_id(pawn1.id), None)
        self.assertEqual(board.get_entity_location(pawn1), (-1, -1))
        self.assertEqual(board.get_entity_at((0, 1)), None)
        self.assertEqual(board.get_entity_by_id(pawn2.id), None)
        self.assertEqual(board.get_entity_location(pawn2), (-1, -1))


if __name__ == "__main__":
    unittest.main()
