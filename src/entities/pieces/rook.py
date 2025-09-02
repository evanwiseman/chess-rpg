from src.constants import (
    ROOK_DAMAGE, ROOK_HEALTH, ROOK_NAME, ROOK_RANGE, ROOK_VALUE,
)

from .piece import Piece


class Rook(Piece):
    def __init__(self):
        super().__init__(ROOK_NAME)
        self.directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        self.stats["value"].base_value = ROOK_VALUE
        self.stats["max_health"].base_value = ROOK_HEALTH
        self.stats["damage"].base_value = ROOK_DAMAGE
        self.stats["range"].base_value = ROOK_RANGE
