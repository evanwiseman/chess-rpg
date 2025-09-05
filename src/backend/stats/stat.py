from typing import Dict, List, Optional
from .modifier import Modifier, ModifierType


class Stat:
    def __init__(
        self,
        name: str,
        base_value: float,
        min_value: float = 0,
        max_value: float = float('inf')
    ):
        self.name = name
        self._base_value = base_value
        self.min_value = min_value
        self.max_value = max_value

        self._modifiers: List[Modifier] = []

        self._cached_value: Optional[float] = None
        self._cache_dirty = True

    def __eq__(self, other: 'Stat'):
        return (
            self.name == other.name
            and self.base_value == other.base_value
            and self.value == other.value
            and self._modifiers == other._modifiers
            and self.min_value == other.min_value
            and self.max_value == other.max_value
            and self._cached_value == other._cached_value
            and self._cache_dirty == other._cache_dirty
        )

    def __repr__(self):
        return f"Stat('{self.name}', '{self.base_value}', '{self.value}')"

    @property
    def base_value(self) -> float:
        return self._base_value

    @base_value.setter
    def base_value(self, value: float):
        self._base_value = value
        self._cache_dirty = True

    @property
    def value(self) -> int:
        if self._cache_dirty or self._cached_value is None:
            self._calculate_value()
        return int(self._cached_value)

    def _calculate_value(self):
        value = self._base_value

        for modifier_type in [
            ModifierType.FLAT,
            ModifierType.PERCENTAGE,
            ModifierType.MULTIPLIER
        ]:
            for modifier in self._modifiers:
                if modifier.modifier_type == modifier_type:
                    value = modifier.apply(value)

        self._cached_value = max(self.min_value, min(self.max_value, value))
        self._cache_dirty = False

    def get_modifier(self, name: str) -> Optional[Modifier]:
        for mod in self._modifiers:
            if mod.name == name:
                return mod
        return None

    def add_modifier(self, modifier: Modifier):
        self._modifiers.append(modifier)
        self._cache_dirty = True

    def remove_modifier(self, modifier: Modifier):
        if modifier in self._modifiers:
            self._modifiers.remove(modifier)
            self._cache_dirty = True

    def remove_modifiers_by_source(self, source: str):
        before = len(self._modifiers)
        self._modifiers = [m for m in self._modifiers if m.source != source]
        if len(self._modifiers) != before:
            self._cache_dirty = True

    def tick(self) -> List[Modifier]:
        expired = []
        for modifier in self._modifiers:
            if modifier.tick():
                expired.append(modifier)
                self.remove_modifier(modifier)
        return expired

    # --- Serialization ---
    def serialize(self) -> Dict:
        return {
            "name": self.name,
            "base_value": self._base_value,
            "min_value": self.min_value,
            "max_value": self.max_value,
            "modifiers": [m.serialize() for m in self._modifiers]
        }

    @classmethod
    def deserialize(cls, data: dict) -> "Stat":
        stat = cls(
            name=data["name"],
            base_value=data["base_value"],
            min_value=data["min_value"],
            max_value=data["max_value"],
        )
        for mod_data in data.get("modifiers", []):
            stat.add_modifier(Modifier.deserialize(mod_data))
        return stat
