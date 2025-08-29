from .constants import (
    PAWN_DAMAGE, PAWN_HEALTH, PAWN_NAME, PAWN_RANGE, PAWN_VALUE,
    BISHOP_DAMAGE, BISHOP_HEALTH, BISHOP_NAME, BISHOP_RANGE, BISHOP_VALUE,
    KNIGHT_DAMAGE, KNIGHT_HEALTH, KNIGHT_NAME, KNIGHT_RANGE, KNIGHT_VALUE,
    ROOK_DAMAGE, ROOK_HEALTH, ROOK_NAME, ROOK_RANGE, ROOK_VALUE,
    QUEEN_DAMAGE, QUEEN_HEALTH, QUEEN_NAME, QUEEN_RANGE, QUEEN_VALUE,
    KING_DAMAGE, KING_RANGE, KING_HEALTH, KING_NAME, KING_VALUE
)
from .entity import Entity
from .stats import Stats


class Piece(Entity):
    def __init__(self, name: str):
        super().__init__(name)
        self.stats = Stats()

    def __eq__(self, other: 'Piece'):
        return (
            self.name == other.name
            and self.stats == other.stats
        )


class Pawn(Piece):
    def __init__(self):
        super().__init__(PAWN_NAME)
        self.stats.add("value", PAWN_VALUE)
        self.stats.add("max_health", PAWN_HEALTH)
        self.stats.add("damage", PAWN_DAMAGE)
        self.stats.add("range", PAWN_RANGE)


class Bishop(Piece):
    def __init__(self):
        super().__init__(BISHOP_NAME)
        self.stats.add("value", BISHOP_VALUE)
        self.stats.add("max_health", BISHOP_HEALTH)
        self.stats.add("damage", BISHOP_DAMAGE)
        self.stats.add("range", BISHOP_RANGE)


class Knight(Piece):
    def __init__(self):
        super().__init__(KNIGHT_NAME)
        self.stats.add("value", KNIGHT_VALUE)
        self.stats.add("max_health", KNIGHT_HEALTH)
        self.stats.add("damage", KNIGHT_DAMAGE)
        self.stats.add("range", KNIGHT_RANGE)


class Rook(Piece):
    def __init__(self):
        super().__init__(ROOK_NAME)
        self.stats.add("value", ROOK_VALUE)
        self.stats.add("max_health", ROOK_HEALTH)
        self.stats.add("damage", ROOK_DAMAGE)
        self.stats.add("range", ROOK_RANGE)


class Queen(Piece):
    def __init__(self):
        super().__init__(QUEEN_NAME)
        self.stats.add("value", QUEEN_VALUE)
        self.stats.add("max_health", QUEEN_HEALTH)
        self.stats.add("damage", QUEEN_DAMAGE)
        self.stats.add("range", QUEEN_RANGE)


class King(Piece):
    def __init__(self):
        super().__init__(KING_NAME)
        self.stats.add("value", KING_VALUE)
        self.stats.add("max_health", KING_HEALTH)
        self.stats.add("damage", KING_DAMAGE)
        self.stats.add("range", KING_RANGE)
