from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional


class ModifierType(Enum):
    """
    Types of modifiers that can be applied to stats.
    """
    FLAT = "flat"
    PERCENTAGE = "percentage"
    MULTIPLIER = "multiplier"


@dataclass
class Modifier:
    name: str
    value: float
    modifier_type: ModifierType
    source: Optional[str] = None
    duration: Optional[int] = None

    def apply(self, value: float) -> float:
        """
        Get the value of the modifier applied.
        """
        match self.modifier_type:
            case ModifierType.FLAT:
                return value + self.value
            case ModifierType.PERCENTAGE:
                return value * (1 + self.value / 100)
            case ModifierType.MULTIPLIER:
                return value * self.value
        return value

    def __eq__(self, other: 'Modifier'):
        return (
            self.name == other.name
            and self.value == other.value
            and self.modifier_type == other.modifier_type
            and self.source == other.source
            and self.duration == other.duration
        )

    def __str__(self) -> str:
        sign = "+" if self.value >= 0 else ""
        if self.modifier_type == ModifierType.FLAT:
            return f"{sign}{self.value}"
        elif self.modifier_type == ModifierType.PERCENTAGE:
            return f"{sign}{self.value}%"
        elif self.modifier_type == ModifierType.MULTIPLIER:
            return f"x{self.value}"

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "value": self.value,
            "modifier_type": self.modifier_type.value,
            "source": self.source,
            "duration": self.duration
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Modifier':
        return cls(
            name=data["name"],
            value=data["value"],
            modifier_type=ModifierType(data["modifier_type"]),
            source=data.get("source"),
            duration=data.get("duration"),
        )
