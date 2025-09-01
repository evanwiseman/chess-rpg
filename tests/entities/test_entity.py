import unittest

from src.entities import Entity


class TestEntity(unittest.TestCase):
    def test_creation(self):
        entity1 = Entity("test1")
        self.assertGreaterEqual(entity1.id, 1)
        self.assertEqual(entity1.name, "test1")
        self.assertEqual(entity1.is_alive, True)

    def test_multiple_entities(self):
        entity2 = Entity("test2")
        entity3 = Entity("test3")
        self.assertGreaterEqual(entity2.id, 2)
        self.assertGreaterEqual(entity3.id, 3)
