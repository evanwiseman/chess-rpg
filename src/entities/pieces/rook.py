from src.constants import (
    ROOK_DAMAGE, ROOK_HEALTH, ROOK_NAME, ROOK_RANGE, ROOK_VALUE,
)

from .piece import Piece


class Rook(Piece):
    def __init__(self):
        super().__init__(ROOK_NAME)
        self.stats.add("value", ROOK_VALUE)
        self.stats.add("max_health", ROOK_HEALTH)
        self.stats.add("damage", ROOK_DAMAGE)
        self.stats.add("range", ROOK_RANGE)
