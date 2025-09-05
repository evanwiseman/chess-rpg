import copy
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from src.backend.core.player import Player


class Entity:
    _next_id = 1   # class-level counter

    def __init__(self, name: str, owner: Optional['Player'] = None):
        self._id = Entity._next_id
        Entity._next_id += 1
        self.name = name
        self._owner = owner

    def __eq__(self, other: 'Entity'):
        return (
            self._id == other._id
        )

    def __repr__(self):
        return f"<Entity {self.name} ({self.id})>"

    def __deepcopy__(self, memo):
        cls = self.__class__
        new_obj = cls.__new__(cls)  # create empty instance
        memo[id(self)] = new_obj

        # copy attributes, but generate new id
        for k, v in self.__dict__.items():
            if k == "_id":
                continue
            setattr(new_obj, k, copy.deepcopy(v, memo))

        new_obj._id = Entity._next_id
        Entity._next_id += 1
        return new_obj

    @property
    def owner(self) -> 'Player':
        return self._owner

    @owner.setter
    def owner(self, new_owner: Optional['Player']):
        self._owner = new_owner

    def same_owner(self, other: 'Entity'):
        return self._owner and other._owner and self._owner == other._owner

    @property
    def id(self) -> int:
        return self._id
