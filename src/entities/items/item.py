from src.entities import Entity


class Item(Entity):
    def __init__(self, name, quantity):
        super().__init__(name)
        self.quantity = quantity
