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
        self.board.place_entity(self.entity, (0, 0))
        self.assertTrue(self.board.contains_entity(self.entity))
        self.assertEqual(self.board.get_entity_position(self.entity), (0, 0))
        self.assertEqual(self.board.get_entity_at((0, 0)), self.entity)

    def test_place_entity_duplicate_entity(self):
        self.board.place_entity(self.entity, (0, 0))
        with self.assertRaises(KeyError):
            self.board.place_entity(self.entity, (1, 1))

    def test_place_entity_same_position(self):
        self.board.place_entity(self.entity, (0, 0))
        other_entity = Entity("other")

        with self.assertRaises(ValueError):
            self.board.place_entity(other_entity, (0, 0))

    def test_place_entity_multiple(self):
        entity1 = Entity("test1")
        self.board.place_entity(entity1, (0, 0))
        entity2 = Entity("test2")
        self.board.place_entity(entity2, (0, 1))
        entity3 = Entity("test3")
        self.board.place_entity(entity3, (0, 2))

        self.assertTrue(self.board.contains_entity(entity1))
        self.assertEqual(self.board.get_entity_position(entity1), (0, 0))

        self.assertTrue(self.board.contains_entity(entity2))
        self.assertEqual(self.board.get_entity_position(entity2), (0, 1))

        self.assertTrue(self.board.contains_entity(entity3))
        self.assertEqual(self.board.get_entity_position(entity3), (0, 2))

    def test_move_entity(self):
        self.board.place_entity(self.entity, (0, 0))
        self.board.move_entity(self.entity, (1, 1))

        self.assertTrue(self.board.contains_entity(self.entity))
        self.assertEqual(self.board.get_entity_position(self.entity), (1, 1))
        self.assertIsNone(self.board.get_entity_at((0, 0)))

    def test_remove_entity(self):
        self.board.place_entity(self.entity, (0, 0))
        self.assertTrue(self.board.remove_entity(self.entity))
        self.assertFalse(self.board.remove_entity(self.entity))

        self.assertFalse(self.board.contains_entity(self.entity))
        with self.assertRaises(KeyError):
            self.board.get_entity_position(self.entity)

    def test_swap_entity(self):
        first = Entity("first")
        second = Entity("second")

        self.board.place_entity(first, (0, 0))
        self.board.place_entity(second, (1, 1))

        self.board.swap_entity(first, second)
        self.assertEqual(self.board.get_entity_position(first), (1, 1))
        self.assertEqual(self.board.get_entity_position(second), (0, 0))


if __name__ == "__main__":
    unittest.main()
