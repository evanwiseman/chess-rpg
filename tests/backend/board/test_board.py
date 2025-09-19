import unittest

from src.backend.board import Board
from src.backend.entities import Entity


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(rows=8, cols=8)
        self.entity = Entity("test")

    def test_creation(self):
        self.assertIsInstance(self.board, Board)

    def test_in_bounds(self):
        self.assertTrue(self.board.in_bounds((0, 0)))
        self.assertTrue(self.board.in_bounds((0, 7)))
        self.assertTrue(self.board.in_bounds((7, 0)))
        self.assertTrue(self.board.in_bounds((7, 7)))
        self.assertFalse(self.board.in_bounds((-1, -1)))
        self.assertFalse(self.board.in_bounds((0, -1)))
        self.assertFalse(self.board.in_bounds((-1, 0)))
        self.assertFalse(self.board.in_bounds((8, 8)))
        self.assertFalse(self.board.in_bounds((7, 8)))
        self.assertFalse(self.board.in_bounds((8, 7)))

    def test_get_size(self):
        self.assertEqual(self.board.get_size(), (8, 8))

    def test_place_entity(self):
        self.board.place_piece(self.entity, (0, 0))
        self.assertTrue(self.board.contains_piece(self.entity))
        self.assertEqual(self.board.get_piece_position(self.entity), (0, 0))
        self.assertEqual(self.board.get_piece_at((0, 0)), self.entity)

    def test_place_entity_duplicate_entity(self):
        self.board.place_piece(self.entity, (0, 0))
        with self.assertRaises(KeyError):
            self.board.place_piece(self.entity, (1, 1))

    def test_place_entity_same_position(self):
        self.board.place_piece(self.entity, (0, 0))
        other_entity = Entity("other")

        with self.assertRaises(ValueError):
            self.board.place_piece(other_entity, (0, 0))

    def test_place_entity_multiple(self):
        entity1 = Entity("test1")
        self.board.place_piece(entity1, (0, 0))
        entity2 = Entity("test2")
        self.board.place_piece(entity2, (0, 1))
        entity3 = Entity("test3")
        self.board.place_piece(entity3, (0, 2))

        self.assertTrue(self.board.contains_piece(entity1))
        self.assertEqual(self.board.get_piece_position(entity1), (0, 0))

        self.assertTrue(self.board.contains_piece(entity2))
        self.assertEqual(self.board.get_piece_position(entity2), (0, 1))

        self.assertTrue(self.board.contains_piece(entity3))
        self.assertEqual(self.board.get_piece_position(entity3), (0, 2))

    def test_move_entity(self):
        self.board.place_piece(self.entity, (0, 0))
        self.board.move_piece(self.entity, (1, 1))

        self.assertTrue(self.board.contains_piece(self.entity))
        self.assertEqual(self.board.get_piece_position(self.entity), (1, 1))
        self.assertIsNone(self.board.get_piece_at((0, 0)))

    def test_remove_entity(self):
        self.board.place_piece(self.entity, (0, 0))
        self.assertTrue(self.board.remove_piece(self.entity))
        self.assertFalse(self.board.remove_piece(self.entity))

        self.assertFalse(self.board.contains_piece(self.entity))
        with self.assertRaises(KeyError):
            self.board.get_piece_position(self.entity)

    def test_swap_entity(self):
        first = Entity("first")
        second = Entity("second")

        self.board.place_piece(first, (0, 0))
        self.board.place_piece(second, (1, 1))

        self.board.swap_piece(first, second)
        self.assertEqual(self.board.get_piece_position(first), (1, 1))
        self.assertEqual(self.board.get_piece_position(second), (0, 0))


if __name__ == "__main__":
    unittest.main()
