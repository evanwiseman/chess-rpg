class Entity:
    _next_id = 1   # class-level counter

    def __init__(self, name: str):
        self._id = Entity._next_id
        Entity._next_id += 1
        self.name = name
        self.is_alive = True

    def __repr__(self):
        return f"<Entity {self.name} ({self.id})>"

    @property
    def id(self) -> int:
        return self._id
