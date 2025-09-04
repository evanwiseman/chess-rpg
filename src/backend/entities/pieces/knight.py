from src.backend.foundation.constants import (
    KNIGHT_HEALTH, KNIGHT_NAME, KNIGHT_RANGE, KNIGHT_VALUE,
)

from .piece import Piece


class Knight(Piece):
    def __init__(self):
        super().__init__(KNIGHT_NAME)
        self._directions = [
            (1, 2),
            (2, 1),
            (2, -1),
            (1, -2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2)
        ]

        self.stats["value"].base_value = KNIGHT_VALUE
        self.stats["max_health"].base_value = KNIGHT_HEALTH
        self.stats["move_range"].base_value = KNIGHT_RANGE

    def get_move_directions(self):
        return self._directions

    def get_action_directions(self):
        return self._directions
