from src.constants import (
    KING_DAMAGE, KING_RANGE, KING_HEALTH, KING_NAME, KING_VALUE
)

from .piece import Piece


class King(Piece):
    def __init__(self):
        super().__init__(KING_NAME)
        self.directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]

        self.stats["value"].base_value = KING_VALUE
        self.stats["max_health"].base_value = KING_HEALTH
        self.stats["attack_damage"].base_value = KING_DAMAGE
        self.stats["move_range"].base_value = KING_RANGE
