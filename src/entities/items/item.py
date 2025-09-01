from src.entities import Entity
from src.stats import Stats


class Item(Entity):
    def __init__(self, name: str, description: str = "", quantity: int = 1):
        super().__init__(name)
        self.is_alive = False
        self.description = description
        self.quantity = quantity
        self.stats = Stats()

    def __eq__(self, other: 'Item'):
        return (
            self.name == other.name
            and self.description == other.description
            and self.quantity == self.quantity
        )
