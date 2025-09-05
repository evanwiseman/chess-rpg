from typing import Optional
from .stat import Stat


class Resource(Stat):
    def __init__(
        self,
        name: str,
        base_value: float,
        current: Optional[float] = None,
        **kwargs
    ):
        super().__init__(name, base_value, **kwargs)
        self._current = current if current is not None else base_value

    @property
    def max(self) -> int:
        """Current max after modifiers (from Stat.value)."""
        return int(self.value)

    @property
    def current(self) -> int:
        return min(int(self._current), self.max)

    @current.setter
    def current(self, val: float):
        self._current = max(0, min(val, self.max))

    # --- Helpers ---
    def take(self, amount: float):
        self.current -= amount

    def give(self, amount: float):
        self.current += amount

    def refill(self):
        self._current = self.value

    def is_depleted(self) -> bool:
        return self.current <= 0

    # --- Serialization ---
    def serialize(self) -> dict:
        data = super().serialize()
        data["current"] = self._current
        return data

    @classmethod
    def deserialize(cls, data: dict) -> "Resource":
        stat = Stat.deserialize(data)
        current = data.get("current", stat.value)
        return cls(
            stat.name,
            stat.base_value, current=current,
            min_value=stat.min_value,
            max_value=stat.max_value
        )
