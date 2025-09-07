import copy
import uuid


class Entity:
    def __init__(
        self,
        name: str,
        entity_id: str = None
    ):
        self.name = name
        self._id = entity_id or uuid.uuid4().hex

    # --- ID ---
    @property
    def id(self) -> str:
        return self._id

    # --- Copying ---
    def clone(self) -> 'Entity':
        """
        Create a copy of this entity.
        By default, assigns a new UUID. Set keep_id=True to keep the same ID.
        """
        new_entity = copy.deepcopy(self)
        new_entity._id = str(uuid.uuid4())
        return new_entity

    # --- Overrides ---
    def __eq__(self, other: 'Entity'):
        return (
            isinstance(other, Entity)
            and self._id == other._id
        )

    def __repr__(self):
        return f"<Entity {self.name} ({self._id})>"
