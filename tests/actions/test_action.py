import unittest
from src.actions import Action
from src.entities import Entity


class TestAction(unittest.TestCase):
    def test_create(self):
        actor = Entity("actor")
        target = Entity("target")
        action = Action(actor, target)

        self.assertIsInstance(action, Action)


if __name__ == "__main__":
    unittest.main()
