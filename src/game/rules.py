from typing import List, Tuple
from src.entities.pieces import Piece
from .board import Board
from .move import Move, MoveType


class Rules:
    @staticmethod
    def get_valid_moves(
        piece: Piece,
        board: Board,
    ) -> List[Move]:
        # Helper function for candidates
        def _process_candidate(candidate: Tuple[int, int]):
            nonlocal location
            if not board.is_in_bounds(candidate):
                return True  # stop ray
            target = board.get_entity_at(candidate)
            if not target:
                moves.append(
                    Move(
                        start=location,
                        end=candidate,
                        move_type=MoveType.MOVE,
                        actor=piece)
                    )
                return False  # continue ray
            return True  # stop ray after hitting any piece

        moves = []
        location = board.get_entity_location(piece)
        for direction in piece.directions:
            for step in range(1, piece.get_move_range() + 1):
                row = location[0] + step * direction[0]
                col = location[1] + step * direction[1]
                candidate = (row, col)
                if _process_candidate(candidate):
                    break
        return moves
