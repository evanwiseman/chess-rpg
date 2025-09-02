from enum import Enum
from typing import Optional, Tuple

from src.entities import Entity


class MoveType(Enum):
    MOVE = "move"
    ATTACK = "attack"
    CASTLE = "castle"
    SPECIAL = "special"


class MoveStatus(Enum):
    COMPLETED = "completed"
    PENDING = "pending"
    FAILED = "failed"


class Move:
    def __init__(
        self,
        start: Tuple[int, int],
        end: Tuple[int, int],
        move_type: MoveType,
        actor: Entity,
        target: Optional[Entity] = None
    ):
        self.start = start
        self.end = end
        self.move_type = move_type
        self.actor = actor
        self.target = target

    def __eq__(self, other: 'Move'):
        return (
            self.start == other.start
            and self.end == other.end
            and self.move_type == other.move_type
            and self.actor == other.actor
            and self.target == other.target
        )

    def __repr__(self):
        return f"<Move {self.move_type} {self.actor} {self.start}->{self.end}>"


class MoveResult:
    def __init__(
        self,
        move: Move,
        status: MoveStatus,
        target: Optional[Entity] = None
    ):
        self.move = move          # original move object
        self.status = status    # whether board was mutated
        self.target = target      # attack or affected entity

    def __eq__(self, other: 'MoveResult'):
        return (
            self.move == other.move
            and self.status == other.status
            and self.target == other.target
        )

    def __repr__(self):
        return (
            f"MoveResult(move={self.move}, "
            f"applied={self.status.name}, "
            f"target={self.target})"
        )
