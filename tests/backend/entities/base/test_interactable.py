import unittest

from src.backend.entities.base import Interactable


class TestInteractable(unittest.TestCase):
    def test_create(self):
        interactable = Interactable("Chest")
        self.assertIsInstance(interactable, Interactable)
        self.assertGreaterEqual(interactable.id, 1)
        self.assertEqual(interactable.name, "Chest")


if __name__ == "__main__":
    unittest.main()
