from typing import Optional


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
