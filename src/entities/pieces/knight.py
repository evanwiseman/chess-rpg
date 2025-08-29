from src.constants import (
    KNIGHT_DAMAGE, KNIGHT_HEALTH, KNIGHT_NAME, KNIGHT_RANGE, KNIGHT_VALUE,
)

from .piece import Piece


class Knight(Piece):
    def __init__(self):
        super().__init__(KNIGHT_NAME)
        self.stats.add("value", KNIGHT_VALUE)
        self.stats.add("max_health", KNIGHT_HEALTH)
        self.stats.add("damage", KNIGHT_DAMAGE)
        self.stats.add("range", KNIGHT_RANGE)
