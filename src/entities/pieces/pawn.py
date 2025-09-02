from src.constants import (
    PAWN_DAMAGE, PAWN_HEALTH, PAWN_NAME, PAWN_RANGE, PAWN_VALUE,
)

from .piece import Piece


class Pawn(Piece):
    def __init__(self):
        super().__init__(PAWN_NAME)

        self.stats["value"].base_value = PAWN_VALUE
        self.stats["max_health"].base_value = PAWN_HEALTH
        self.stats["damage"].base_value = PAWN_DAMAGE
        self.stats["range"].base_value = PAWN_RANGE
