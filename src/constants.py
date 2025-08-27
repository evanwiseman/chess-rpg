import copy

from .stats import Stats, MovementType

PAWN_HP = 10
PAWN_DAMAGE = 5
PAWN_MOVEMENT_RANGE = 1
PAWN_MOVEMENT_TYPES = {MovementType.FORWARD}
PAWN_STATS = Stats(
    hp=PAWN_HP,
    damage=PAWN_DAMAGE,
    movement_range=PAWN_MOVEMENT_RANGE,
    movement_types=copy.copy(PAWN_MOVEMENT_TYPES)
)

BISHOP_HP = 30
BISHOP_DAMAGE = 15
BISHOP_MOVEMENT_RANGE = None
BISHOP_MOVEMENT_TYPES = {MovementType.DIAGONAL}
BISHOP_STATS = Stats(
    hp=BISHOP_HP,
    damage=BISHOP_DAMAGE,
    movement_range=BISHOP_MOVEMENT_RANGE,
    movement_types=copy.copy(BISHOP_MOVEMENT_TYPES)
)

KNIGHT_HP = 30
KNIGHT_DAMAGE = 15
KNIGHT_MOVEMENT_RANGE = None
KNIGHT_MOVEMENT_TYPES = {MovementType.L_SHAPE}
KNIGHT_STATS = Stats(
    hp=KNIGHT_HP,
    damage=KNIGHT_DAMAGE,
    movement_range=KNIGHT_MOVEMENT_RANGE,
    movement_types=copy.copy(KNIGHT_MOVEMENT_TYPES)
)

ROOK_HP = 50
ROOK_DAMAGE = 25
ROOK_MOVEMENT_RANGE = None
ROOK_MOVEMENT_TYPES = {
    MovementType.FORWARD,
    MovementType.BACKWARD,
    MovementType.LEFT,
    MovementType.RIGHT
}
ROOK_STATS = Stats(
    hp=ROOK_HP,
    damage=ROOK_DAMAGE,
    movement_range=ROOK_MOVEMENT_RANGE,
    movement_types=copy.copy(ROOK_MOVEMENT_TYPES)
)

QUEEN_HP = 90
QUEEN_DAMAGE = 45
QUEEN_MOVEMENT_RANGE = None
QUEEN_MOVEMENT_TYPES = {
    MovementType.FORWARD,
    MovementType.BACKWARD,
    MovementType.LEFT,
    MovementType.RIGHT,
    MovementType.DIAGONAL
}
QUEEN_STATS = Stats(
    hp=QUEEN_HP,
    damage=QUEEN_DAMAGE,
    movement_range=QUEEN_MOVEMENT_RANGE,
    movement_types=copy.copy(QUEEN_MOVEMENT_TYPES)
)

KING_HP = 80
KING_DAMAGE = 10
KING_MOVEMENT_RANGE = 1
KING_MOVEMENT_TYPES = {
    MovementType.FORWARD,
    MovementType.BACKWARD,
    MovementType.LEFT,
    MovementType.RIGHT,
    MovementType.DIAGONAL
}
KING_STATS = Stats(
    hp=KING_HP,
    damage=KING_DAMAGE,
    movement_range=KING_MOVEMENT_RANGE,
    movement_types=copy.copy(KING_MOVEMENT_TYPES)
)
