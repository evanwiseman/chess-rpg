import unittest
from src.actions import Move, MoveType
from src.entities import Entity


class TestMove(unittest.TestCase):
    def test_create(self):
        actor = Entity("actor")
        move = Move(
            (0, 0),
            (1, 1),
            MoveType.MOVE,
            actor
        )

        self.assertIsInstance(move, Move)
        self.assertEqual(move.start, (0, 0))
        self.assertEqual(move.end, (1, 1))
        self.assertEqual(move.move_type, MoveType.MOVE)
        self.assertEqual(move.actor, actor)

    def test_eq(self):
        actor = Entity("actor")
        move1 = Move(
            (0, 0),
            (1, 1),
            MoveType.MOVE,
            actor
        )
        move2 = Move(
            (0, 0),
            (1, 1),
            MoveType.MOVE,
            actor
        )

        self.assertEqual(move1, move2)


if __name__ == "__main__":
    unittest.main()
