from dataclasses import dataclass
from typing import Optional
from src.backend.foundation.enums import ModifierType


@dataclass
class Modifier:
    name: str
    value: float
    modifier_type: ModifierType
    source: Optional[str] = None
    duration: Optional[int] = None

    def apply(self, value: float) -> float:
        if self.modifier_type == ModifierType.FLAT:
            return value + self.value
        elif self.modifier_type == ModifierType.PERCENTAGE:
            return value * (1 + self.value / 100)
        elif self.modifier_type == ModifierType.MULTIPLIER:
            return value * self.value
        return value

    def tick(self) -> bool:
        """Decrement duration, return True if expired."""
        if self.duration is not None:
            self.duration -= 1
            return self.duration <= 0
        return False

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

    # --- Serialization ---
    def serialize(self) -> dict:
        return {
            "name": self.name,
            "value": self.value,
            "modifier_type": self.modifier_type.value,
            "source": self.source,
            "duration": self.duration
        }

    @classmethod
    def deserialize(cls, data: dict) -> 'Modifier':
        return cls(
            name=data["name"],
            value=data["value"],
            modifier_type=ModifierType(data["modifier_type"]),
            source=data.get("source"),
            duration=data.get("duration")
        )
