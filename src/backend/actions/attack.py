from dataclasses import dataclass
from enum import Enum


class AttackType(Enum):
    PHYSICAL = "PHYSICAL"
    MAGIC = "MAGIC"


@dataclass
class Attack:
    name: str
    attack_type: AttackType
    base_damage: int

    @property
    def damage(self) -> int:
        return self.base_damage
