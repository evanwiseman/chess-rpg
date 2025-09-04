from typing import Dict, List

from .modifier import Modifier
from .stat import Stat


class Stats:
    """
    Container for multiple stats with convenient access methods.
    Behaves like a dict: stats["health"] -> Stat
    """

    def __init__(self):
        self._stats: Dict[str, Stat] = {}

    def __eq__(self, other: 'Stats'):
        return (
            self._stats == other._stats
        )

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

    def serialize(self) -> dict:
        return {name: stat.to_dict() for name, stat in self._stats.items()}

    @classmethod
    def deserialize(cls, data: dict) -> 'Stats':
        stats = cls()
        for name, stat_data in data.items():
            stats[name] = Stat.from_dict(stat_data)
        return stats

    def __str__(self) -> str:
        return "Stats:\n" + "\n".join(f"  {s}" for s in self._stats.values())
