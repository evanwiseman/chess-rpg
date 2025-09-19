from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.backend.board import Board
    from src.backend.entities.pieces import Piece
from src.backend.foundations.types import Vector2


class Action(ABC):
    def __init__(self, actor: 'Piece'):
        self.actor = actor

    @abstractmethod
    def execute(self, board: 'Board'):
        raise NotImplementedError


class MoveAction(Action):
    def __init__(self, actor: 'Piece', position: Vector2):
        super().__init__(actor)
        self.position = position

    def execute(self, board: 'Board'):
        board.move_piece(self.actor, self.position)


class AttackAction(Action):
    def __init__(self, actor: 'Piece', damage: int, target: 'Piece'):
        super().__init__(actor)
        self.damage = damage
        self.target = target

    def execute(self, board: 'Board'):
        self.target.take_damage(self.damage)
