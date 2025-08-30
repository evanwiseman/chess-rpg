from src.stats import Stats

from .item import Item


class Equipment(Item):
    def __init__(self, name, quantity):
        super().__init__(name, quantity)
        self.stats = Stats()
