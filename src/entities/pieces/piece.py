from src.entities import Entity
from src.stats import Stats


class Piece(Entity):
    def __init__(self, name: str):
        super().__init__(name)
        self.stats = Stats()

    def __eq__(self, other: 'Piece'):
        return (
            self.name == other.name
            and self.stats == other.stats
        )
