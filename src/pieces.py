from .stats import Stats
from .entity import Entity


class Piece(Entity):
    def __init__(self, id: int, name: str):
        super().__init__(id, name)
        self.stats = Stats()


class Pawn(Piece):
    def __init__(self, name: str = "Pawn"):
        super().__init__(name)


class Bishop(Piece):
    def __init__(self, name: str = "Bishop"):
        super().__init__(name)


class Knight(Piece):
    def __init__(self, name: str = "Knight"):
        super().__init__(name)


class Rook(Piece):
    def __init__(self, name: str = "Rook"):
        super().__init__(name)


class Queen(Piece):
    def __init__(self, name: str = "Queen"):
        super().__init__(name)


class King(Piece):
    def __init__(self, name: str = "King"):
        super().__init__(name)
