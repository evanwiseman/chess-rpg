from src.constants import (
    QUEEN_HEALTH, QUEEN_NAME, QUEEN_RANGE, QUEEN_VALUE,
)

from .piece import Piece


class Queen(Piece):
    def __init__(self):
        super().__init__(QUEEN_NAME)
        self._directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]
        self.stats["value"].base_value = QUEEN_VALUE
        self.stats["max_health"].base_value = QUEEN_HEALTH
        self.stats["move_range"].base_value = QUEEN_RANGE

    def get_move_directions(self):
        return self._directions

    def get_action_directions(self):
        return self._directions
