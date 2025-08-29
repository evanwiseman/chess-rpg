# from .stats import Stats
from .entity import Entity


class Piece(Entity):
    def __init__(self, name: str, value: int):
        super().__init__(name)
        self.value = value


class Pawn(Piece):
    def __init__(self, name: str = "Pawn"):
        super().__init__(name, 1)


class Bishop(Piece):
    def __init__(self, name: str = "Bishop"):
        super().__init__(name, 3)


class Knight(Piece):
    def __init__(self, name: str = "Knight"):
        super().__init__(name, 3)


class Rook(Piece):
    def __init__(self, name: str = "Rook"):
        super().__init__(name, 5)


class Queen(Piece):
    def __init__(self, name: str = "Queen"):
        super().__init__(name, 9)


class King(Piece):
    def __init__(self, name: str = "King"):
        super().__init__(name, 100)
