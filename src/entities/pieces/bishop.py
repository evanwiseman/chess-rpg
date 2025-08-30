from src.constants import (
    BISHOP_DAMAGE, BISHOP_HEALTH, BISHOP_NAME, BISHOP_RANGE, BISHOP_VALUE
)

from .piece import Piece


class Bishop(Piece):
    def __init__(self):
        super().__init__(BISHOP_NAME)
        self.stats.add("value", BISHOP_VALUE)
        self.stats.add("max_health", BISHOP_HEALTH)
        self.stats.add("damage", BISHOP_DAMAGE)
        self.stats.add("range", BISHOP_RANGE)
