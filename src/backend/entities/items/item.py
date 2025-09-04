from src.backend.entities.base import Interactable


class Item(Interactable):
    def __init__(self, name: str, description: str = "", quantity: int = 1):
        super().__init__(name)
        self.is_alive = False
        self.description = description
        self.quantity = quantity

    def __eq__(self, other: 'Item'):
        return (
            self.name == other.name
            and self.description == other.description
            and self.quantity == self.quantity
        )
