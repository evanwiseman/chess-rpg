from src.backend.entities.base import Entity
from src.backend.stats import StatsManager, ResourceManager
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.backend.core.player import Player


class Piece(Entity):
    def __init__(self, name, owner: 'Player' = None):
        super().__init__(name, owner)

        self.stats = StatsManager()
        self.resources = ResourceManager()
