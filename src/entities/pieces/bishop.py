from src.constants import (
    BISHOP_DAMAGE, BISHOP_HEALTH, BISHOP_NAME, BISHOP_RANGE, BISHOP_VALUE
)

from .piece import Piece


class Bishop(Piece):
    def __init__(self):
        super().__init__(BISHOP_NAME)
        self.directions = [
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]

        self.stats["value"].base_value = BISHOP_VALUE
        self.stats["max_health"].base_value = BISHOP_HEALTH
        self.stats["damage"].base_value = BISHOP_DAMAGE
        self.stats["range"].base_value = BISHOP_RANGE
