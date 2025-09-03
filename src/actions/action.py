from enum import Enum
from typing import Optional
from src.entities import Entity


class ActionType(Enum):
    ATTACK = "attack"
    SPELL = "spell"
    ITEM = "item"
    OTHER = "other"


class Action:
    def __init__(
        self,
        actor: Entity,
        payload: object,
        target: Optional[Entity] = None
    ):
        self.actor = actor
        self.payload = payload
        self.target = target
        self._type = ActionType.OTHER

    @property
    def type(self):
        return self._type

    def __eq__(self, other: 'Action'):
        if not isinstance(other, Action):
            return False
        return (
            self.actor == other.actor
            and self.payload == other.payload
            and self.target == other.target
            and self.type == other.type
        )

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}("
            f"actor={self.actor}, payload={self.payload}, "
            f"target={self.target}, type={self.type})>"
        )
