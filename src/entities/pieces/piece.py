from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from src.game import Player
from src.actions import AttackBook, SpellBook
from src.entities import Entity
from src.stats import Resource, Stat, Stats
from src.systems import EquipmentManager


class Piece(Entity):
    def __init__(self, name: str, owner: Optional['Player'] = None):
        super().__init__(name, owner)
        self._moved = False

        self.stats = Stats()
        self.stats["value"] = Stat("Value", 0)
        self.stats["move_range"] = Stat("Move Range", 0)

        # Set resource pool linked to stats
        self.stats["max_health"] = Stat("Max Health", 0)
        self.health = Resource(lambda: self.stats["max_health"].value)
        self.stats["max_mana"] = Stat("Max Mana", 0)
        self.mana = Resource(lambda: self.stats["max_mana"].value)
        self.stats["max_stamina"] = Stat("Max Stamina", 0)
        self.stamina = Resource(lambda: self.stats["max_stamina"].value)

        self.spell_book = SpellBook()
        self.attack_book = AttackBook()
        self._equipment_manager = EquipmentManager()

    # Movement methods
    def get_move_directions(self):
        raise NotImplementedError

    def get_action_directions(self):
        raise NotImplementedError

    def get_move_range(self):
        return self.stats["move_range"].value

    def get_moved(self) -> bool:
        return self._moved

    def set_moved(self, state: bool):
        self._moved = state

    # Resource Methods
    def take_damage(self, amount: int):
        self.health.take(amount)

    def heal(self, amount: int):
        self.health.give(amount)

    def is_alive(self):
        return not self.health.is_depleted()

    def use_mana(self, amount: int):
        self.mana.take(amount)

    def restore_mana(self, amount: int):
        self.mana.give(amount)
