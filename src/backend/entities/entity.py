import copy
import uuid


class Entity:
    def __init__(self, name, id: str = None):
        self.name = name
        self._id = id or uuid.uuid4().hex

    @property
    def id(self) -> str:
        return self._id

    def __copy__(self) -> 'Entity':
        """
        Create a shallow copy of entity. Keeps ID.
        """
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo) -> 'Entity':
        """
        Create a deep copy fo entity. Generates a new ID.
        """
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k == "_id":
                setattr(result, k, uuid.uuid4().hex)
            else:
                setattr(result, k, copy.deepcopy(v, memo))
        return result

    def __eq__(self, other: 'Entity'):
        """
        Entities are considered equal if they have the same id

        Args:
            other (Entity): Entity to compare.
        """
        return self.id == other.id

    def __repr__(self) -> str:
        return f"<Entity name='{self.name}', id='{self.id}'>"
