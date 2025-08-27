import copy

from .constants import (
    PAWN_STATS, BISHOP_STATS, KNIGHT_STATS, ROOK_STATS,
    QUEEN_STATS, KING_STATS
)
from .stats import Stats


class Piece:
    def __init__(self, stats: Stats):
        # Create deep copies so we don't overwrite a reference
        self.__base_stats = copy.deepcopy(stats)
        self.__stats = copy.deepcopy(stats)

    @property
    def stats(self) -> Stats | None:
        return self.__stats

    @stats.setter
    def stats(self, value: Stats):
        self.__stats = value

    def reset_stats(self):
        self.__stats = copy.deepcopy(self.__base_stats)

    def is_alive(self):
        return self.stats.hp > 0

    def take_damage(self, damage):
        self.stats.hp -= damage


class Pawn(Piece):
    def __init__(self, stats: Stats = PAWN_STATS):
        super().__init__(stats)


class Bishop(Piece):
    def __init__(self, stats: Stats = BISHOP_STATS):
        super().__init__(stats)


class Knight(Piece):
    def __init__(self, stats: Stats = KNIGHT_STATS):
        super().__init__(stats)


class Rook(Piece):
    def __init__(self, stats: Stats = ROOK_STATS):
        super().__init__(stats)


class Queen(Piece):
    def __init__(self, stats: Stats = QUEEN_STATS):
        super().__init__(stats)


class King(Piece):
    def __init__(self, stats: Stats = KING_STATS):
        super().__init__(stats)
