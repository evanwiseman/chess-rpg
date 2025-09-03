from enum import Enum
from typing import Tuple

from src.entities import Entity


class MoveType(Enum):
    MOVE = "move"
    SPECIAL = "special"


class Move:
    def __init__(
        self,
        start: Tuple[int, int],
        end: Tuple[int, int],
        move_type: MoveType,
        actor: Entity,
    ):
        self.start = start
        self.end = end
        self.move_type = move_type
        self.actor = actor

    def __eq__(self, other: 'Move'):
        return (
            self.start == other.start
            and self.end == other.end
            and self.move_type == other.move_type
            and self.actor == other.actor
        )

    def __repr__(self):
        return f"<Move {self.move_type} {self.actor} {self.start}->{self.end}>"
