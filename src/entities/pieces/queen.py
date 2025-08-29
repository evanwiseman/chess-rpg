from src.constants import (
    QUEEN_DAMAGE, QUEEN_HEALTH, QUEEN_NAME, QUEEN_RANGE, QUEEN_VALUE,
)

from .piece import Piece


class Queen(Piece):
    def __init__(self):
        super().__init__(QUEEN_NAME)
        self.stats.add("value", QUEEN_VALUE)
        self.stats.add("max_health", QUEEN_HEALTH)
        self.stats.add("damage", QUEEN_DAMAGE)
        self.stats.add("range", QUEEN_RANGE)
