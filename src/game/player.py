from enum import Enum
from typing import Dict, Optional, Tuple
from src.entities.pieces import Piece
from src.systems import ItemManager


class Team(Enum):
    WHITE = "white",
    BLACK = "black"


class Player:
    def __init__(
        self,
        name: str,
        team: Team,
        forward: Optional[Tuple[int, int]] = None
    ):
        self.name = name
        self.team = team

        if forward is not None:
            self.forward = forward
        elif self.team == Team.WHITE:
            self.forward = (-1, 0)
        else:
            self.forward = (1, 0)

        self.pieces: Dict[int, Piece] = {}
        self.inventory = ItemManager()

    def __eq__(self, other: 'Player'):
        return self.team == other.team

    def add_piece(self, piece: Piece):
        piece._owner = self
        self.pieces[piece.id] = piece

    def remove_piece(self, piece: Piece):
        if piece.id in self.pieces:
            del self.pieces[piece.id]

    def issue_move(self, piece: Piece):
        raise NotImplementedError

    def issue_action(self, piece: Piece):
        raise NotImplementedError

    def owns(self, piece: Piece) -> bool:
        return piece.id in self.pieces
