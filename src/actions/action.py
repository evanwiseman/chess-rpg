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
        target: Optional[Entity] = None
    ):
        self.actor = actor
        self.target = target

    @property
    def type(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}("
            f"actor={self.actor} target={self.target})>"
        )
