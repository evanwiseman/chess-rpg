from typing import List
from src.backend.foundations.types import Vector2
from .piece import Piece


class Rook(Piece):
    def __init__(self, name: str = "Rook", id: str = None):
        super().__init__(name, id)
        self.hp = 50

    def get_move_range(self) -> int:
        return 8

    def get_move_directions(self) -> List[Vector2]:
        return [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]

    def get_attack_range(self) -> int:
        return 8

    def get_attack_directions(self) -> List[Vector2]:
        return [
            ((1, 0), (-1, 0), (0, 1), (0, -1))
        ]

    def get_damage(self) -> int:
        return 25

    def take_damage(self, amount):
        self.hp -= amount
