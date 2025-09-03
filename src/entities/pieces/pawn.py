from src.constants import (
    PAWN_HEALTH, PAWN_NAME, PAWN_RANGE, PAWN_VALUE,
)

from .piece import Piece


class Pawn(Piece):
    def __init__(self):
        super().__init__(PAWN_NAME)

        self.stats["value"].base_value = PAWN_VALUE
        self.stats["max_health"].base_value = PAWN_HEALTH
        self.stats["move_range"].base_value = PAWN_RANGE

    def get_move_directions(self):
        directions = []
        if self.owner:
            directions.append(self.owner.forward)
        return directions

    def get_action_directions(self):
        directions = []
        if self.owner:
            row, col = self.owner.forward
            if (abs(row)):
                directions.append((row, col + 1))
                directions.append((row, col - 1))
            elif (abs(col)):
                directions.append((row + 1, col))
                directions.append((row - 1, col))
        return directions

    def get_move_range(self):
        if self._moved:
            return super().get_move_range()
        else:
            return super().get_move_range() + 1
