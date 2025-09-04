from .entity import Entity


class Interactable(Entity):
    def __init__(self, name):
        super().__init__(name)
