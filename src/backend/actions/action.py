from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.backend.board import Board
    from src.backend.entities import Entity
from src.backend.foundations.types import Vector2
from .attack import Attack


class Action(ABC):
    def __init__(self, actor: 'Entity'):
        self.actor = actor

    @abstractmethod
    def can_perform(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def execute(self, board: 'Board'):
        raise NotImplementedError


class MoveAction(Action):
    def __init__(self, actor: 'Entity', position: Vector2):
        super().__init__(actor)
        self.position = position

    def execute(self, board: 'Board'):
        board.move_entity(self.actor, self.position)


class AttackAction(Action):
    def __init__(self, actor: 'Entity', attack: Attack, target: 'Entity'):
        super().__init__(actor)
        self.attack = attack
        self.target = target

    def execute(self, board: 'Board'):
        pass
