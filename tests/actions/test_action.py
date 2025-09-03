import unittest
from src.actions import Action
from src.entities import Entity


class TestAction(unittest.TestCase):
    def test_create(self):
        actor = Entity("actor")
        target = Entity("target")
        action = Action(actor, target)

        self.assertIsInstance(action, Action)

    def test_type(self):
        actor = Entity("actor")
        target = Entity("target")
        action = Action(actor, target)

        self.assertRaises(NotImplementedError, lambda: action.type)

    def test_eq(self):
        actor = Entity("actor")
        target = Entity("target")
        action1 = Action(actor, target)
        action2 = Action(actor, target)

        self.assertRaises(NotImplementedError, lambda: action1 == action2)


if __name__ == "__main__":
    unittest.main()
