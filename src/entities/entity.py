from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from src.game import Player


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
