import copy
import uuid
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from src.backend.core.player import Player


class Entity:
    def __init__(
        self,
        name: str,
        owner: Optional['Player'] = None,
        entity_id: str = None
    ):
        self.name = name
        self._owner = owner
        self._id = entity_id or uuid.uuid4().hex

    # --- ID ---
    @property
    def id(self) -> str:
        return self._id

    # --- Owner ---
    @property
    def owner(self) -> Optional['Player']:
        return self._owner

    @owner.setter
    def owner(self, new_owner: Optional['Player']):
        self._owner = new_owner

    def same_owner(self, other: 'Entity'):
        return self.owner and other.owner and self.owner == other.owner

    # --- Copying ---
    def clone(
        self,
        new_owner: Optional['Player'] = None,
        keep_id: bool = False
    ) -> 'Entity':
        """
        Create a copy of this entity.
        By default, assigns a new UUID. Set keep_id=True to keep the same ID.
        """
        new_entity = copy.deepcopy(self)
        if not keep_id:
            new_entity._id = str(uuid.uuid4())
        if new_owner is not None:
            new_entity._owner = new_owner
        return new_entity

    # --- Overrides ---
    def __eq__(self, other: 'Entity'):
        return (
            isinstance(other, Entity)
            and self._id == other._id
        )

    def __repr__(self):
        return f"<Entity {self.name} ({self._id})>"
