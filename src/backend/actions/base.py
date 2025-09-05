from abc import ABC, abstractmethod
from typing import Optional, Tuple, TYPE_CHECKING
from src.backend.foundation import ActionCategory, ActionResult
if TYPE_CHECKING:
    from src.backend.entities.base import Entity


class BaseAction(ABC):
    category: ActionCategory = ActionCategory.MOVE
    requires_target: bool = False

    def __init__(
        self,
        actor: 'Entity',
        target: Optional['Entity'] = None,
        target_pos: Optional[Tuple[int, int]] = None,
        **kwargs
    ):
        self.actor = actor
        self.target = target
        self.target_pos = target_pos
        self.metadata = kwargs

    @abstractmethod
    def can_execute(self) -> bool:
        """Each action knows its own validation rules."""
        raise NotImplementedError

    @abstractmethod
    def execute(self):
        """Each action handles its own execution logic."""
        raise NotImplementedError
