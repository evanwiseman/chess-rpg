from typing import Tuple, List

from src.actions import AttackBook, SpellBook
from src.entities import Entity
from src.stats import Resource, Stat, Stats
from src.systems import EquipmentManager


class Piece(Entity):
    def __init__(self, name: str):
        super().__init__(name)
        self.directions: List[Tuple[int, int]] = []

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

    def __eq__(self, other: 'Piece'):
        return (
            self.name == other.name
            and self.stats == other.stats
        )

    def get_move_range(self):
        return self.stats["move_range"].value

    def get_attack_range(self):
        return self.stats["attack_range"].value

    def get_interact_range(self):
        return self.stats["interact_range"].value

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
