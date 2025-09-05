from typing import Dict
from .stat import Stat


class StatsManager:
    """
    Container for multiple stats with convenient access methods.
    """

    def __init__(self):
        self._stats: Dict[str, Stat] = {}

    # --- Helper ---
    def _normalize_name(self, name: str):
        return name.lower()

    # --- Accessors/Mutators ---
    def add(self, name: str, base: float, **kwargs):
        stat = Stat(name, base, **kwargs)
        self.add_stat(stat)

    def add_stat(self, stat: Stat):
        key = self._normalize_name(stat.name)
        self._stats[key] = stat

    def get_stat(self, name: str) -> Stat:
        key = self._normalize_name(name)
        if key not in self._stats:
            raise KeyError(f"Stat {name} not found")
        return self._stats[key]

    def contains_stat(self, name: str) -> bool:
        key = self._normalize_name(name)
        return key in self._stats

    # --- Convenience ---
    def __getitem__(self, name: str):
        """Dict-like access"""
        key = self._normalize_name(name)
        if key in self._stats:
            return self._stats[key]
        raise KeyError(f"'{name}' not found in stats")

    def __contains__(self, name: str) -> bool:
        key = self._normalize_name(name)
        return key in self._stats

    def __repr__(self):
        stats = ", ".join(f"{k}={v.value}" for k, v in self._stats.items())
        return f"<Stats stats=[{stats}]>"

    def serialize(self) -> dict:
        return {
            "stats": {
                name: stat.serialize()
                for name, stat in self._stats.items()
            }
        }

    @classmethod
    def deserialize(cls, data: Dict) -> 'StatsManager':
        mgr = cls()
        for stat_data in data.get("stats", {}).values():
            stat = Stat.deserialize(stat_data)
            mgr.add_stat(stat)
        return mgr
