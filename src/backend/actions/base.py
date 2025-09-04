from typing import Any, Optional, TYPE_CHECKING
from src.backend.foundation import ActionType

if TYPE_CHECKING:
    from src.backend.entities.base import Entity


class Action:
    def __init__(
        self,
        actor: 'Entity',
        payload: Any,
        target: Optional['Entity'] = None,
        type: ActionType = ActionType.OTHER
    ):
        self.actor = actor
        self.payload = payload
        self.target = target
        self._type = type

    @property
    def type(self):
        return self._type

    def can_execute(self) -> bool:
        """Check if this action can be executed."""
        pass

    def execute(self) -> bool:
        """Execute this action."""
        pass

    def __eq__(self, other: 'Action'):
        if not isinstance(other, Action):
            return False
        return (
            self.actor == other.actor
            and self.payload == other.payload
            and self.target == other.target
            and self.type == other.type
        )

    def __repr__(self) -> str:
        """String representation of the action."""
        # Safe attribute access since these might not exist
        if self.actor:
            actor_name = getattr(self.actor, "name", str(self.actor))
        else:
            actor_name = "None"

        if self.target:
            target_name = getattr(self.target, "name", str(self.target))
        else:
            target_name = "None"

        return (
            f"<{self.__class__.__name__}("
            f"actor={actor_name}, "
            f"payload={self.payload}, "
            f"target={target_name}, "
            f"type={self.type.name})>"
        )
