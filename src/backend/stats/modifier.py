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
    """
    Container to hold modifier data.
    """
    name: str
    value: float
    modifier_type: ModifierType
    source: Optional[str] = None
    duration: Optional[int] = None

    def apply(self, value: float) -> float:
        """
        Apply the modifer to value and return new value.
        """
        if self.modifier_type == ModifierType.FLAT:
            return value + self.value
        elif self.modifier_type == ModifierType.PERCENTAGE:
            return value * (1 + self.value / 100)
        elif self.modifier_type == ModifierType.MULTIPLIER:
            return value * self.value
        return value

    def tick(self) -> bool:
        """
        Decrement duration, return True if expired.
        """
        if self.duration is not None:
            self.duration -= 1
            return self.duration <= 0
        return False

    # --- Serialization ---
    def serialize(self) -> Dict:
        return {
            "name": self.name,
            "value": self.value,
            "modifier_type": self.modifier_type.value,
            "source": self.source,
            "duration": self.duration
        }

    @classmethod
    def deserialize(cls, data: Dict) -> 'Modifier':
        return cls(
            name=data["name"],
            value=data["value"],
            modifier_type=ModifierType(data["modifier_type"]),
            source=data.get("source"),
            duration=data.get("duration")
        )

    # --- Overrides ---
    def __eq__(self, other: 'Modifier'):
        return (
            self.name == other.name
            and self.value == other.value
            and self.modifier_type == other.modifier_type
            and self.source == other.source
            and self.duration == other.duration
        )

    def __repr__(self) -> str:
        if self.modifier_type == ModifierType.FLAT:
            return f"{self.value:+}"
        elif self.modifier_type == ModifierType.PERCENTAGE:
            return f"{self.value:+}%"
        elif self.modifier_type == ModifierType.MULTIPLIER:
            return f"x{self.value}"
