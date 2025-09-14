from src.backend.entities import Entity


class Piece(Entity):
    def __init__(self, name, id: str = None):
        super().__init__(name, id)

    def take_damage(self, amount):
        raise NotImplementedError
