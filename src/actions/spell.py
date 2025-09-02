from typing import Optional
from src.entities import Entity
from .action import Action, ActionType


class Spell:
    def __init__(
        self,
        name: str,
        description: str,
        damage: int,
        mana_cost: int,
        cast_range: int,
        cooldown: int,
        area_of_effect: Optional[int] = None
    ):
        self.name = name
        self.description = description
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range
        self.cooldown = cooldown
        self.area_of_effect = area_of_effect


class SpellAction(Action):
    def __init__(
        self,
        actor: Entity,
        spell: Spell,
        target: Optional[Entity] = None
    ):
        super().__init__(actor, target)
        self.spell = spell

    @property
    def type(self):
        return ActionType.SPELL
