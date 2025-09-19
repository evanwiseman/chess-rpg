from typing import List
from src.backend.foundations.types import Vector2
from .piece import Piece


class King(Piece):
    def __init__(self, name: str = "King", id: str = None):
        super().__init__(name, id)
        self.hp = 100

    def get_move_range(self) -> int:
        return 1

    def get_move_directions(self) -> List[Vector2]:
        return [
            (1, 1), (1, 0), (1, -1),
            (0, 1), (0, -1),
            (-1, 1), (-1, 0), (-1, -1)
        ]

    def get_attack_range(self) -> int:
        return 1

    def get_attack_directions(self) -> List[Vector2]:
        return [
            (1, 1), (1, 0), (1, -1),
            (0, 1), (0, -1),
            (-1, 1), (-1, 0), (-1, -1)
        ]

    def get_damage(self) -> int:
        return 10

    def take_damage(self, amount):
        self.hp -= amount
