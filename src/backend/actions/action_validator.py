from .action import AttackAction, MoveAction
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from src.backend.board import Board
    from src.backend.entities.pieces import Piece


class ActionValidator:
    def __init__(self, board: 'Board'):
        self.board = board

    def get_valid_moves(self, piece: 'Piece') -> List[MoveAction]:
        moves = []
        position = self.board.get_piece_position(piece)
        for dx, dy in piece.get_move_directions():
            for i in range(piece.get_move_range()):
                row = position[0] + dy * i
                col = position[1] + dx * i

                # Out of bounds
                if not self.board.in_bounds((row, col)):
                    break
                # Piece already at location
                if self.board.get_piece_at((row, col)):
                    break

                moves.append(MoveAction(piece, (row, col)))
        return moves

    def get_valid_attacks(self, piece: 'Piece') -> List[AttackAction]:
        attacks = []
        position = self.board.get_piece_position(piece)
        for dx, dy in piece.get_move_directions():
            for i in range(piece.get_attack_range()):
                row = position[0] + dy * i
                col = position[1] + dx * i

                # Out of bounds
                if not self.board.in_bounds((row, col)):
                    break

                target = self.board.get_piece_at((row, col))
                # No target at position
                if not target:
                    continue
                attacks.append(AttackAction(piece, piece.get_damage(), target))
        return attacks
