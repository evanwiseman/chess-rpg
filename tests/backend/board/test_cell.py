import unittest
from src.backend.board.cell import Cell
from src.backend.entities.pieces import Piece
from src.backend.items import Item


class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell = Cell()
        self.piece = Piece("piece")
        self.item = Item("item")

    def test_initial_state_empty(self):
        self.assertTrue(self.cell.is_empty())
        self.assertFalse(self.cell.has_piece())
        self.assertFalse(self.cell.has_item())

    def test_place_piece(self):
        self.cell.piece = self.piece
        self.assertFalse(self.cell.is_empty())
        self.assertTrue(self.cell.has_piece())
        self.assertFalse(self.cell.has_item())

    def test_place_item(self):
        self.cell.item = self.item
        self.assertFalse(self.cell.is_empty())
        self.assertFalse(self.cell.has_piece())
        self.assertTrue(self.cell.has_item())

    def test_place_piece_and_item(self):
        self.cell.piece = self.piece
        self.cell.item = self.item
        self.assertFalse(self.cell.is_empty())
        self.assertTrue(self.cell.has_piece())
        self.assertTrue(self.cell.has_item())

    def test_clear_cell(self):
        self.cell.piece = self.piece
        self.cell.item = self.item
        self.cell.clear()
        self.assertTrue(self.cell.is_empty())
        self.assertFalse(self.cell.has_piece())
        self.assertFalse(self.cell.has_item())


if __name__ == "__main__":
    unittest.main()
