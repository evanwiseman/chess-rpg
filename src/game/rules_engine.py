from typing import List, Tuple, Optional
from src.actions import Action, AttackAction, SpellAction, Move, MoveType
from src.entities import Entity
from src.entities.pieces import Piece
from .board import Board


class RulesEngine:
    @staticmethod
    def _validate_target(actor: Entity, target: Optional[Entity]):
        return (
            target and target != actor
        )

    @staticmethod
    def get_valid_moves(
        piece: Piece,
        board: Board,
    ) -> List[Move]:
        location = board.get_entity_location(piece)
        moves = []

        # Helper function for candidates
        def _process_candidate(candidate: Tuple[int, int]):
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

        for direction in piece.get_move_directions():
            for step in range(1, piece.get_move_range() + 1):
                row = location[0] + step * direction[0]
                col = location[1] + step * direction[1]
                candidate = (row, col)
                if _process_candidate(candidate):
                    break
        return moves

    @staticmethod
    def get_valid_actions(piece: Piece, board: Board) -> List[Action]:
        location = board.get_entity_location(piece)
        actions: List[Action] = []

        def _raycast_targets(max_range: int) -> List[Tuple[int, int]]:
            """
            Return all reachable locations in range or until entity reached.
            """
            targets = []
            for direction in piece.get_action_directions():
                for step in range(1, max_range + 1):
                    row = location[0] + step * direction[0]
                    col = location[1] + step * direction[1]
                    candidate = (row, col)
                    if not board.is_in_bounds(candidate):
                        break
                    target_entity = board.get_entity_at(candidate)
                    # Stop ray if a piece is encountered
                    targets.append(candidate)
                    if target_entity is not None:
                        break
            return targets

        # Attack actions
        for attack in piece.attack_book.all_attacks():
            for target_pos in _raycast_targets(attack.attack_range):
                target_entity = board.get_entity_at(target_pos)
                if not RulesEngine._validate_target(piece, target_entity):
                    continue
                actions.append(
                    AttackAction(
                        actor=piece,
                        attack=attack,
                        target=target_entity
                    )
                )

        # Spell actions
        for spell in piece.spell_book.all_spells():
            for target_pos in _raycast_targets(spell.cast_range):
                target_entity = board.get_entity_at(target_pos)
                if not RulesEngine._validate_target(piece, target_entity):
                    continue
                actions.append(
                    SpellAction(
                        actor=piece,
                        spell=spell,
                        target=target_entity
                    )
                )

        return actions
