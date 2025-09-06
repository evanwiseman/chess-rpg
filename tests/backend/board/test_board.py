import unittest
from src.backend.board import Board
from src.backend.entities.pieces import Piece
from src.backend.items import Item


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(rows=8, cols=8)
        self.pawn = Piece("pawn")
        self.king = Piece("king")
        self.item = Item("Health Potion")

    # --- Piece Tests ---
    def test_place_and_get_piece(self):
        self.board.place_piece((0, 0), self.pawn)
        piece = self.board.get_piece_at((0, 0))
        self.assertEqual(piece, self.pawn)

    def test_place_piece_already_occupied(self):
        self.board.place_piece((0, 0), self.pawn)
        with self.assertRaises(ValueError):
            self.board.place_piece((0, 0), self.king)

    def test_remove_piece(self):
        self.board.place_piece((0, 0), self.pawn)
        self.board.remove_piece(self.pawn)
        self.assertIsNone(self.board.get_piece_at((0, 0)))

    def test_remove_piece_at(self):
        self.board.place_piece((0, 0), self.pawn)
        self.board.remove_piece_at((0, 0))
        self.assertIsNone(self.board.get_piece_at((0, 0)))

    def test_move_piece(self):
        self.board.place_piece((0, 0), self.pawn)
        self.board.move_piece((0, 0), (1, 0))
        self.assertIsNone(self.board.get_piece_at((0, 0)))
        self.assertEqual(self.board.get_piece_at((1, 0)), self.pawn)

    def test_move_piece_to_occupied(self):
        self.board.place_piece((0, 0), self.pawn)
        self.board.place_piece((1, 0), self.king)
        with self.assertRaises(ValueError):
            self.board.move_piece((0, 0), (1, 0))

    # --- Item Tests ---
    def test_place_and_get_item(self):
        self.board.place_item((2, 2), self.item)
        item = self.board.get_item_at((2, 2))
        self.assertEqual(item, self.item)

    def test_place_item_already_occupied(self):
        self.board.place_item((2, 2), self.item)
        new_item = Item("Mana Potion")
        with self.assertRaises(ValueError):
            self.board.place_item((2, 2), new_item)

    def test_remove_item(self):
        self.board.place_item((2, 2), self.item)
        self.board.remove_item(self.item)
        self.assertIsNone(self.board.get_item_at((2, 2)))

    def test_remove_item_at(self):
        self.board.place_item((2, 2), self.item)
        self.board.remove_item_at((2, 2))
        self.assertIsNone(self.board.get_item_at((2, 2)))

    # --- Bounds / Entity Map Tests ---
    def test_is_in_bounds(self):
        self.assertTrue(self.board.is_in_bounds((0, 0)))
        self.assertTrue(self.board.is_in_bounds((7, 7)))
        self.assertFalse(self.board.is_in_bounds((8, 0)))
        self.assertFalse(self.board.is_in_bounds((-1, 0)))

    def test_get_entity_location(self):
        self.board.place_piece((0, 0), self.pawn)
        loc = self.board.get_entity_location(self.pawn)
        self.assertEqual(loc, (0, 0))
        self.board.remove_piece(self.pawn)
        with self.assertRaises(KeyError):
            self.board.get_entity_location(self.pawn)

    def test_clear_cell(self):
        self.board.place_piece((0, 0), self.pawn)
        self.board.place_item((0, 0), self.item)
        self.board.clear_cell((0, 0))
        self.assertIsNone(self.board.get_piece_at((0, 0)))
        self.assertIsNone(self.board.get_item_at((0, 0)))


if __name__ == "__main__":
    unittest.main()
