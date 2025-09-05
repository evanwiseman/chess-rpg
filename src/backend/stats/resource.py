from typing import Optional
from .stat import Stat


class Resource(Stat):
    """
    Container for a resource, holds modifiers, and calculates current value.
    Inherits from Stat.
    """
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
        """
        Current max after modifiers (from Stat.value).
        """
        return int(self.value)

    @property
    def current(self) -> int:
        """
        Get the current value, clamps to self.max.
        """
        return min(int(self._current), self.max)

    @current.setter
    def current(self, val: float):
        """
        Set the current value, is clamped between 0 and self.max.
        """
        self._current = max(0, min(val, self.max))

    # --- Helpers ---
    def take(self, amount: float):
        """
        Take a specified amount.
        """
        self.current -= amount

    def give(self, amount: float):
        """
        Give a specified amount.
        """
        self.current += amount

    def refill(self):
        """
        Set current to self.max
        """
        self._current = self.max

    def is_depleted(self) -> bool:
        """
        Check if resource has reached 0 or lower
        """
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
        res = cls(
            stat.name,
            stat.base_value,
            current=current,
            min_value=stat.min_value,
            max_value=stat.max_value
        )
        # Copy modifiers from deserialized stat
        for mod in stat._modifiers:
            res.add_modifier(mod)
        return res
