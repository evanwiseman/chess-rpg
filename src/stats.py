from dataclasses import dataclass
from enum import Enum
from typing import Optional, List, Dict, Set


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
            "modifier_type": self.modifier_type,
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
            "modifiers": [m.to_dict() for m in self._modifiers.values()],
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Stat':
        stat = cls(
            name=data["name"],
            base_value=data["base_value"],
            min_value=data.get("min_value", 0),
            max_value=data.get("max_value", float("inf")),
        )
        for mod_data in data.get("modifiers", []):
            stat.add_modifier(Modifier.from_dict(mod_data))
        return stat


class Stats:
    """
    Container for multiple stats with convenient access methods.
    Behaves like a dict: stats["health"] -> Stat
    """

    def __init__(self):
        self._stats: Dict[str, Stat] = {}

    def __getitem__(self, name: str) -> Stat:
        """Dict-like access (case-insensitive)."""
        stat = self._stats.get(name.lower())
        if stat is None:
            raise KeyError(f"Stat '{name}' not found")
        return stat

    def __setitem__(self, name: str, stat: Stat):
        """Assign a Stat directly."""
        self._stats[name.lower()] = stat

    def __contains__(self, name: str) -> bool:
        return name.lower() in self._stats

    def __iter__(self):
        return iter(self._stats.keys())

    def __len__(self) -> int:
        return len(self._stats)

    def add(self, name: str, base_value: float, **kwargs) -> Stat:
        """
        Create and add a new stat.
        Example: stats.add("health", 100, min_value=0, max_value=200)
        """
        stat = Stat(name, base_value, **kwargs)
        self[name] = stat
        return stat

    def update_durations(self) -> Dict[str, List[Modifier]]:
        """
        Tick durations for all stats, returning expired modifiers per stat.
        """
        expired = {}
        for name, stat in self._stats.items():
            expired_mods = stat.update_durations()
            if expired_mods:
                expired[name] = expired_mods
        return expired

    def to_dict(self) -> dict:
        return {name: stat.to_dict() for name, stat in self._stats.items()}

    @classmethod
    def from_dict(cls, data: dict) -> 'Stats':
        stats = cls()
        for name, stat_data in data.items():
            stats[name] = Stat.from_dict(stat_data)
        return stats

    def __str__(self) -> str:
        return "Stats:\n" + "\n".join(f"  {s}" for s in self._stats.values())
