from typing import Dict, List, Optional, Set

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

        # Modifier name mapped to Modifier
        self._modifiers: Dict[str, Modifier] = {}

        # Source mapped to Modifier name
        self._sources: Dict[str, Set[str]] = {}

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
    def value(self) -> float:
        if self._cache_dirty or self._cached_value is None:
            self._calculate_value()
        return self._cached_value

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

        value = max(self.min_value, min(self.max_value, value))
        self._cached_value = value
        self._cache_dirty = False

    def add_modifier(self, modifier: Modifier):
        """Add or replace a modifier by name, tracking its source."""
        if modifier.source is None:
            modifier.source = "global"

        # if replacing, remove old source mapping
        if modifier.name in self._modifiers:
            old_source = self._modifiers[modifier.name].source
            if old_source in self._sources:
                self._sources[old_source].discard(modifier.name)
            if not self._sources[old_source]:
                del self._sources[old_source]

        self._modifiers[modifier.name] = modifier

        if modifier.source not in self._sources:
            self._sources[modifier.source] = set()
        self._sources[modifier.source].add(modifier.name)

        self._cache_dirty = True

    def remove_modifier(self, name: str) -> bool:
        """Remove a modifier by name."""
        if name in self._modifiers:
            source = self._modifiers[name].source
            del self._modifiers[name]
            if source in self._sources:
                self._sources[source].discard(name)
                if not self._sources[source]:
                    del self._sources[source]
            self._cache_dirty = True
            return True
        return False

    def remove_modifiers_by_source(self, source: str) -> bool:
        """Remove all modifiers from a given source (e.g., item unequipped)."""
        if source not in self._sources:
            return False
        for name in list(self._sources[source]):
            del self._modifiers[name]
        del self._sources[source]
        self._cache_dirty = True
        return True

    def update_durations(self) -> List[Modifier]:
        """Tick durations, return expired modifiers."""
        expired = []
        for name, modifier in list(self._modifiers.items()):
            if modifier.duration is not None:
                modifier.duration -= 1
                if modifier.duration <= 0:
                    expired.append(modifier)
                    self.remove_modifier(name)
        return expired

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "base_value": self._base_value,
            "min_value": self.min_value,
            "max_value": self.max_value,
            # store modifiers as name -> dict
            "modifiers": {
                name: mod.to_dict() for name, mod in self._modifiers.items()
            },
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Stat':
        stat = cls(
            name=data["name"],
            base_value=data["base_value"],
            min_value=data.get("min_value", 0),
            max_value=data.get("max_value", float("inf")),
        )
        for name, mod_data in data.get("modifiers", {}).items():
            stat.add_modifier(Modifier.from_dict(mod_data))
        return stat
