from typing import Dict
from src.entities.pieces import Piece
from .team import Team


class Player:
    def __init__(self, team: Team):
        self.team = team
        self.pieces: Dict[int, Piece] = {}

    def add_piece(self, piece: Piece):
        self.pieces[piece.id] = piece

    def remove_piece(self, piece_id: int):
        if piece_id in self.pieces:
            del self.pieces[piece_id]

    def owns(self, piece_id: int) -> bool:
        return piece_id in self.pieces
