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
        area_of_effect: Optional[int] = None,
    ):
        self.name = name
        self.description = description
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range
        self.cooldown = cooldown
        self.area_of_effect = area_of_effect

    def __eq__(self, other: 'Spell'):
        return (
            self.name == other.name
            and self.description == other.description
            and self.damage == other.damage
            and self.mana_cost == other.mana_cost
            and self.cast_range == other.cast_range
            and self.cooldown == other.cooldown
            and self.area_of_effect == other.area_of_effect
        )

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}(name={self.name})>"
        )


class SpellAction(Action):
    def __init__(
        self,
        actor: Entity,
        spell: Spell,
        target: Optional[Entity] = None
    ):
        super().__init__(actor, target)
        self.spell = spell

    def __eq__(self, other: 'SpellAction'):
        return (
            self.actor == other.actor
            and self.spell == other.spell
            and self.target == other.target
        )

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}("
            f"actor={self.actor}, attack={self.spell}, target={self.target})>"
        )

    @property
    def type(self):
        return ActionType.SPELL
