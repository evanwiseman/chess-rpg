import copy
import unittest

from src.backend.entities import Entity


class TestEntity(unittest.TestCase):
    def setUp(self):
        self.entity = Entity("test")

    def test_creation(self):
        self.assertEqual(self.entity.name, "test")
        self.assertIsNotNone(self.entity.id)

    def test_copy(self):
        entity_copy = copy.copy(self.entity)
        self.assertEqual(self.entity.name, entity_copy.name)
        self.assertEqual(self.entity.id, entity_copy.id)
        self.assertEqual(self.entity, entity_copy)

    def test_deep_copy(self):
        entity_deep = copy.deepcopy(self.entity)
        self.assertEqual(self.entity.name, entity_deep.name)
        self.assertNotEqual(self.entity.id, entity_deep.id)
        self.assertNotEqual(self.entity, entity_deep)

    def test_repr(self):
        entity = Entity("test", "id")
        self.assertEqual(str(entity), "<Entity name='test', id='id'>")


if __name__ == "__main__":
    unittest.main()
