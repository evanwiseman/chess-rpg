from src.entities import Entity
from src.stats import Stats


class Item(Entity):
    def __init__(self, name: str, description: str, quantity: int = 1):
        super().__init__(name)
        self.description = description
        self.quantity = quantity
        self.stats = Stats()
