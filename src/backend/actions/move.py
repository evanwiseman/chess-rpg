from typing import Tuple

from src.backend.entities.base import Entity
from src.backend.foundation import MoveType


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
