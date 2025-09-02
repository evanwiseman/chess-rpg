from typing import Callable


class Resource:
    def __init__(self, stat_getter: Callable):
        """
        Creates a new resource

        Args:
            stat_getter: a callable that returns the current_ max
        """
        self._stat_getter = stat_getter
        self._current = stat_getter()

    @property
    def max(self) -> int:
        return self._stat_getter()

    @property
    def current(self) -> int:
        return min(self._current, self.max)

    @current.setter
    def current(self, value: int):
        self._current = max(0, min(value, self.max))

    def take(self, amount: int):
        if amount < 0:
            raise ValueError(
                "Error: (Resource.take) cannot take negative amount."
            )
        self.current -= amount

    def give(self, amount: int):
        if amount < 0:
            raise ValueError(
                "Error: (Resource.give) cannot give negative amount"
            )
        self.current += amount

    def is_depleted(self) -> bool:
        return self.current <= 0

    def refill(self):
        self.current = self.max

    def __repr__(self):
        return f"<Resource {self.current}/{self.max}>"
