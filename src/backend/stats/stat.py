from collections import defaultdict
from typing import Dict, List, Optional, Set, Union
from .modifier import Modifier, ModifierType


class Stat:
    """
    Represents a single stat than can have modifiers applied.
    """
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

        self._modifiers: Dict[str, Modifier] = {}
        self._sources: Dict[str, Set[str]] = defaultdict(Set[str])

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
            and self._sources == other._sources
            and self._cached_value == other._cached_value
            and self._cache_dirty == other._cache_dirty
        )

    def __repr__(self):
        return f"Stat('{self.name}', '{self.base_value}', '{self.value}')"

    @property
    def base_value(self) -> float:
        """
        Get the base value.
        """
        return self._base_value

    @base_value.setter
    def base_value(self, value: float):
        """
        Set the base value and invalidate the cache.
        """
        self._base_value = value
        self._cache_dirty = True

    @property
    def value(self) -> int:
        if self._cache_dirty or self._cached_value is None:
            self._calculate_value()
        return int(self._cached_value)

    def _calculate_value(self):
        """
        Calculate the final value after applying modifiers.
        """
        value = self._base_value

        for modifier_type in [
            ModifierType.FLAT,
            ModifierType.PERCENTAGE,
            ModifierType.MULTIPLIER
        ]:
            for modifier in self._modifiers.values():
                if modifier.modifier_type == modifier_type:
                    value = modifier.apply(value)

        self._cached_value = max(self.min_value, min(self.max_value, value))
        self._cache_dirty = False

    def add_modifier(
        self,
        mod: Union[Modifier, str, int, float],
        name: Optional[str] = None,
        source: Optional[str] = None,
        duration: Optional[int] = None
    ):
        """
        Add modifer with Modifier, str, int, or float.
        If not adding with Modifier must provide a name.
        """
        if isinstance(mod, Modifier):
            modifier = mod
        elif isinstance(mod, str):
            if not name:
                raise ValueError("Modifiers from shorthand require a name")

            if mod.endswith("%"):               # Percentage
                modifier = Modifier(
                    name,
                    float(mod.strip("%")),
                    ModifierType.PERCENTAGE,
                    source,
                    duration
                )
            elif mod.startswith("x"):           # Mutliplier
                modifier = Modifier(
                    name,
                    float(mod[1:]),
                    ModifierType.MULTIPLIER,
                    source,
                    duration
                )
            else:                               # Flat
                modifier = Modifier(
                    name,
                    float(mod),
                    ModifierType.FLAT,
                    source,
                    duration
                )
        elif isinstance(mod, (int, float)):     # Flat
            modifier = Modifier(
                name,
                float(mod),
                ModifierType.FLAT,
                source,
                duration
            )
        else:
            raise TypeError("Invalid modifier type")

        self._modifiers[modifier.name] = modifier
        if modifier.source:
            self._sources[modifier.name].add(modifier.name)
        self._cache_dirty = True

    def remove_modifier(self, name: str) -> bool:
        """Remove a modifier by name."""
        if name in self._modifiers:
            source = self._modifiers[name].source
            del self._modifiers[name]
            if source and source in self._sources:
                self._sources[source].discard(name)
                if not self._sources[source]:
                    del self._sources[source]
            self._cache_dirty = True

    def remove_modifiers_by_source(self, source: str) -> bool:
        """Remove all modifiers from a given source (e.g., item unequipped)."""
        if source not in self._sources:
            return False
        for name in list(self._sources[source]):
            del self._modifiers[name]
        del self._sources[source]
        self._cache_dirty = True

    def tick(self) -> List[Modifier]:
        expired = []
        for name, mod in list(self._modifiers.items()):
            if mod.tick():
                expired.append(name)
                self.remove_modifier(name)
        return expired

    # --- Serialization ---
    def serialize(self) -> dict:
        return {
            "name": self.name,
            "base_value": self._base_value,
            "min_value": self.min_value,
            "max_value": self.max_value,
            "modifiers": {
                name: modifier.serialize()
                for name, modifier in self._modifiers.items()
            }
        }

    @classmethod
    def deserialize(cls, data: dict) -> 'Stat':
        stat = cls(
            name=data["name"],
            base_value=data["base_value"],
            min_value=data["min_value"],
            max_value=data["max_value"]
        )

        for mod_data in data.get("modifiers", {}).values():
            stat.add_modifier(Modifier.deserialize(mod_data))
        return stat
