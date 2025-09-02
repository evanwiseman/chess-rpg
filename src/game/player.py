from enum import Enum
from typing import Dict
from src.entities.pieces import Piece
from src.systems import ItemManager


class Team(Enum):
    WHITE = 1,
    BLACK = -1


class Player:
    def __init__(self, team: Team):
        self.team = team
        self.pieces: Dict[int, Piece] = {}
        self.inventory = ItemManager()

    def add_piece(self, piece: Piece):
        self.pieces[piece.id] = piece

    def remove_piece(self, piece: Piece):
        if piece.id in self.pieces:
            del self.pieces[piece.id]

    def owns(self, piece: Piece) -> bool:
        return piece.id in self.pieces
