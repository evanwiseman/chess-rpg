from typing import List, Optional, Tuple, TYPE_CHECKING
from src.backend.board import Board
from src.backend.actions import Move, Action
from .rules_engine import RulesEngine
from .player import Player
if TYPE_CHECKING:
    from src.backend.entities.pieces import Piece


class GameEngine:
    def __init__(self, players: List[Player], board: Optional[Board] = None):
        self.players = players
        self.board = board or Board()
        self.turn_index = 0  # index in self.players
        self.turn_number = 1

    @property
    def current_player(self) -> Player:
        return self.players[self.turn_index]

    def next_turn(self):
        self.turn_index = (self.turn_index + 1) % len(self.players)
        self.turn_number += 1

    def move_piece(self, piece: 'Piece', target_pos: Tuple[int, int]):
        if piece not in self.current_player.pieces:
            raise ValueError(
                "Cannot move a piece that does not belong to current player"
            )

        valid_moves = RulesEngine.get_valid_moves(piece, self.board)
        piece_location = self.board.get_entity_location(piece)
        move = Move(piece_location, target_pos, None, piece)

        if move not in valid_moves:
            raise ValueError(f"Move to {target_pos} is invalid for {piece}")

        self.board.move_piece(piece_location, target_pos)

    def perform_action(self, action: Action):
        raise NotImplementedError

    def is_game_over(self) -> bool:
        # Simplest example: game over if a player has no pieces
        for player in self.players:
            if not player.pieces:
                return True
        return False

    def get_winner(self) -> Optional[Player]:
        alive_players = [p for p in self.players if p.pieces]
        if len(alive_players) == 1:
            return alive_players[0]
        return None
