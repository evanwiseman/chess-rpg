from .constants import (
    MoveType,
    PAWN_DAMAGE, PAWN_HEALTH, PAWN_NAME, PAWN_MOVE_RANGE,
    PAWN_MOVE_TYPE,
    BISHOP_DAMAGE, BISHOP_HEALTH, BISHOP_NAME, BISHOP_MOVE_RANGE,
    BISHOP_MOVE_TYPE,
    KNIGHT_DAMAGE, KNIGHT_HEALTH, KNIGHT_NAME, KNIGHT_MOVE_RANGE,
    KNIGHT_MOVE_TYPE,
    ROOK_DAMAGE, ROOK_HEALTH, ROOK_NAME, ROOK_MOVE_RANGE,
    ROOK_MOVE_TYPE,
    QUEEN_DAMAGE, QUEEN_HEALTH, QUEEN_NAME, QUEEN_MOVE_RANGE,
    QUEEN_MOVE_TYPE,
    KING_DAMAGE, KING_HEALTH, KING_NAME, KING_MOVE_RANGE, KING_MOVE_TYPE,
)
from stats import Stats


class Piece:
    def __init__(
        self,
        name: str,
        health: int,
        damage: int,
        move_range: int,
        move_type: MoveType
    ):
        self.name = name
        self.stats = Stats()

    def take_damage(self, amount: int):
        if amount < 0:
            raise ValueError("Error: can't take negative damage")
        self.current_health = max(0, self.current_health - amount)

    def heal(self, amount: int):
        if amount < 0:
            raise ValueError("Error: can't heal a negative amount")
        self.current_health += amount

    def __repr__(self):
        return (
            f"{self.name}:\n"
            + f"- health='{self.current_health}'/'{self.max_health}'\n"
            + f"- damage='{self.damage}'\n"
            + f"- move_range='{self.move_range}'\n"
            + f"- move_types='{self.move_type.name}'"
        )


class Pawn(Piece):
    def __init__(self, name: str = PAWN_NAME):
        super().__init__(
            name,
            PAWN_HEALTH,
            PAWN_DAMAGE,
            PAWN_MOVE_RANGE,
            PAWN_MOVE_TYPE
        )


class Bishop(Piece):
    def __init__(self, name: str = BISHOP_NAME):
        super().__init__(
            name,
            BISHOP_HEALTH,
            BISHOP_DAMAGE,
            BISHOP_MOVE_RANGE,
            BISHOP_MOVE_TYPE
        )


class Knight(Piece):
    def __init__(self, name: str = KNIGHT_NAME):
        super().__init__(
            name,
            KNIGHT_HEALTH,
            KNIGHT_DAMAGE,
            KNIGHT_MOVE_RANGE,
            KNIGHT_MOVE_TYPE
        )


class Rook(Piece):
    def __init__(self, name: str = ROOK_NAME):
        super().__init__(
            name,
            ROOK_HEALTH,
            ROOK_DAMAGE,
            ROOK_MOVE_RANGE,
            ROOK_MOVE_TYPE
        )


class Queen(Piece):
    def __init__(self, name: str = QUEEN_NAME):
        super().__init__(
            name,
            QUEEN_HEALTH,
            QUEEN_DAMAGE,
            QUEEN_MOVE_RANGE,
            QUEEN_MOVE_TYPE
        )


class King(Piece):
    def __init__(self, name: str = KING_NAME):
        super().__init__(
            name,
            KING_HEALTH,
            KING_DAMAGE,
            KING_MOVE_RANGE,
            KING_MOVE_TYPE
        )
