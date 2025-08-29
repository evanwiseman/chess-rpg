from src.constants import (
    PAWN_DAMAGE, PAWN_HEALTH, PAWN_NAME, PAWN_RANGE, PAWN_VALUE,
)

from .piece import Piece


class Pawn(Piece):
    def __init__(self):
        super().__init__(PAWN_NAME)
        self.stats.add("value", PAWN_VALUE)
        self.stats.add("max_health", PAWN_HEALTH)
        self.stats.add("damage", PAWN_DAMAGE)
        self.stats.add("range", PAWN_RANGE)

    def promote(self, piece_type: type, *args, **kwargs):
        return piece_type(*args, **kwargs)
