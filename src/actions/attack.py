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


class AttackAction(Action):
    def __init__(
        self,
        actor: Entity,
        attack: Attack,
        target: Optional[Entity] = None
    ):
        super().__init__(actor, target)
        self.attack = attack

    @property
    def type(self):
        return ActionType.ATTACK
