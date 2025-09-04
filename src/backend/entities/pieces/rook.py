from src.backend.foundation.constants import (
    ROOK_HEALTH, ROOK_NAME, ROOK_RANGE, ROOK_VALUE,
)

from .piece import Piece


class Rook(Piece):
    def __init__(self):
        super().__init__(ROOK_NAME)
        self._directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        self.stats["value"].base_value = ROOK_VALUE
        self.stats["max_health"].base_value = ROOK_HEALTH
        self.stats["move_range"].base_value = ROOK_RANGE

    def get_move_directions(self):
        return self._directions

    def get_action_directions(self):
        return self._directions
