from typing import List
from src.backend.foundations.types import Vector2
from .piece import Piece


class Knight(Piece):
    def __init__(self, name, id: str = None):
        super().__init__(name, id)
        self.hp = 30

    def get_move_range(self) -> int:
        return 1

    def get_move_directions(self) -> List[Vector2]:
        return [
            (2, 1), (1, 2), (-2, 1), (-1, 2),
            (2, -1), (1, -2), (-2, -1), (-1, -2)
        ]

    def get_attack_range(self) -> int:
        return 1

    def get_attack_directions(self) -> List[Vector2]:
        return [
            (2, 1), (1, 2), (-2, 1), (-1, 2),
            (2, -1), (1, -2), (-2, -1), (-1, -2)
        ]

    def get_damage(self) -> int:
        return 15

    def take_damage(self, amount):
        self.hp -= amount
