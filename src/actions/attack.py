from typing import Optional
from src.entities import Entity
from .action import Action, ActionType


class Attack:
    def __init__(
        self,
        name: str,
        description: str,
        damage: int,
        stamina_cost: int,
        attack_range: int,
        cooldown: int,
        area_of_effect: Optional[int] = None
    ):
        self.name = name
        self.description = description
        self.damage = damage
        self.stamina_cost = stamina_cost
        self.attack_range = attack_range
        self.cooldown = cooldown
        self.area_of_effect = area_of_effect

    def __eq__(self, other: 'Attack'):
        return (
            self.name == other.name
            and self.description == other.description
            and self.damage == other.damage
            and self.stamina_cost == other.stamina_cost
            and self.attack_range == other.attack_range
            and self.cooldown == other.cooldown
            and self.area_of_effect == other.area_of_effect
        )

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}(name={self.name})>"
        )


class AttackAction(Action):
    def __init__(
        self,
        actor: Entity,
        attack: Attack,
        target: Optional[Entity] = None
    ):
        super().__init__(actor, target)
        self.attack = attack

    def __eq__(self, other: 'AttackAction'):
        return (
            self.actor == other.actor
            and self.attack == other.attack
            and self.target == other.target
            and self.type == other.type
        )

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}("
            f"actor={self.actor}, attack={self.attack}, target={self.target})>"
        )

    @property
    def type(self):
        return ActionType.ATTACK
