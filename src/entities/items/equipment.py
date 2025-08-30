from .item import Item


class Equipment(Item):
    def __init__(self, name, description: str, quantity: int = 1):
        super().__init__(name, quantity)
