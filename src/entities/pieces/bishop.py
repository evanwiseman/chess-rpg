from src.constants import (
    BISHOP_HEALTH, BISHOP_NAME, BISHOP_RANGE, BISHOP_VALUE
)

from .piece import Piece


class Bishop(Piece):
    def __init__(self):
        super().__init__(BISHOP_NAME)
        self._directions = [
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]

        self.stats["value"].base_value = BISHOP_VALUE
        self.stats["max_health"].base_value = BISHOP_HEALTH
        self.stats["move_range"].base_value = BISHOP_RANGE

    def get_move_directions(self):
        return self._directions

    def get_action_directions(self):
        return self._directions
