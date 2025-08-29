from src.constants import (
    KING_DAMAGE, KING_RANGE, KING_HEALTH, KING_NAME, KING_VALUE
)

from .piece import Piece


class King(Piece):
    def __init__(self):
        super().__init__(KING_NAME)
        self.stats.add("value", KING_VALUE)
        self.stats.add("max_health", KING_HEALTH)
        self.stats.add("damage", KING_DAMAGE)
        self.stats.add("range", KING_RANGE)
