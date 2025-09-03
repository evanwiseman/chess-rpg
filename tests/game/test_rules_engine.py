import unittest
from typing import Type, Tuple

from src.actions import (
    Attack, AttackAction, Spell, SpellAction, Move, MoveType
)
from src.board import Board
from src.game import RulesEngine, Team, Player
from src.entities.pieces import (
    Piece, Pawn, Bishop, Knight, Rook, Queen, King
)


class RulesTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white = Player("white", Team.WHITE)
        self.black = Player("black", Team.BLACK)

    def place_piece(
        self,
        piece_cls: Type[Piece],
        player: Player,
        pos: Tuple[int, int]
    ) -> Piece:
        """Helper to create, add to player, and place on board."""
        piece = piece_cls()
        player.add_piece(piece)
        self.board.place_piece(pos, piece)
        return piece

    def add_attack(
        self,
        piece: Piece,
        name="Slash",
        damage=10,
        cost=5,
        rng=1,
        cd=1
    ) -> Attack:
        attack = Attack(
            name=name,
            description="",
            damage=damage,
            stamina_cost=cost,
            attack_range=rng,
            cooldown=cd,
        )
        piece.attack_book.add_attack(attack)
        return attack

    def add_spell(
        self,
        piece: Piece,
        name="Magic Missile",
        dmg=30,
        mana=10,
        rng=3,
        cd=3
    ) -> Spell:
        spell = Spell(
            name=name,
            description="",
            damage=dmg,
            mana_cost=mana,
            cast_range=rng,
            cooldown=cd,
        )
        piece.spell_book.add_spell(spell)
        return spell


class TestRulesMoves(RulesTestCase):
    def test_bishop_moves(self):
        bishop = self.place_piece(Bishop, self.white, (4, 4))
        moves = RulesEngine.get_valid_moves(bishop, self.board)
        # Test corners reachable
        expected = [(0, 0), (7, 7), (1, 7), (7, 1)]
        for pos in expected:
            self.assertIn(Move((4, 4), pos, MoveType.MOVE, bishop), moves)

    def test_bishop_obstructed(self):
        bishop = self.place_piece(Bishop, self.white, (7, 2))
        self.place_piece(Pawn, self.white, (6, 3))
        self.place_piece(Pawn, self.white, (6, 1))
        moves = RulesEngine.get_valid_moves(bishop, self.board)
        self.assertEqual(moves, [])

    def test_knight_moves(self):
        knight = self.place_piece(Knight, self.white, (4, 4))
        moves = RulesEngine.get_valid_moves(knight, self.board)
        expected = [
            (2, 3), (3, 2), (5, 6), (6, 5), (6, 3), (5, 2), (2, 5), (3, 6)
        ]
        for pos in expected:
            self.assertIn(Move((4, 4), pos, MoveType.MOVE, knight), moves)

    def test_pawn_moves_first_and_second(self):
        pawn = self.place_piece(Pawn, self.white, (6, 4))
        moves_first = RulesEngine.get_valid_moves(pawn, self.board)
        self.assertIn(Move((6, 4), (5, 4), MoveType.MOVE, pawn), moves_first)
        self.assertIn(Move((6, 4), (4, 4), MoveType.MOVE, pawn), moves_first)

        pawn2 = self.place_piece(Pawn, self.white, (5, 4))
        pawn2.set_moved(True)
        moves_second = RulesEngine.get_valid_moves(pawn2, self.board)
        self.assertIn(Move((5, 4), (4, 4), MoveType.MOVE, pawn2), moves_second)
        self.assertNotIn(
            Move((5, 4), (3, 4), MoveType.MOVE, pawn2),
            moves_second
        )

    def test_rook_moves(self):
        rook = self.place_piece(Rook, self.white, (4, 4))
        moves = RulesEngine.get_valid_moves(rook, self.board)
        self.assertIn(Move((4, 4), (4, 0), MoveType.MOVE, rook), moves)
        self.assertIn(Move((4, 4), (0, 4), MoveType.MOVE, rook), moves)

    def test_queen_moves(self):
        queen = self.place_piece(Queen, self.white, (4, 4))
        moves = RulesEngine.get_valid_moves(queen, self.board)
        self.assertIn(Move((4, 4), (4, 0), MoveType.MOVE, queen), moves)
        self.assertIn(Move((4, 4), (0, 4), MoveType.MOVE, queen), moves)


class TestRulesActions(RulesTestCase):
    def test_attack_and_spell_single_target(self):
        bishop = self.place_piece(Bishop, self.white, (4, 4))
        pawn = self.place_piece(Pawn, self.black, (3, 3))
        attack = self.add_attack(bishop, rng=1)
        spell = self.add_spell(bishop, rng=3)

        actions = RulesEngine.get_valid_actions(bishop, self.board)
        self.assertIn(AttackAction(bishop, attack, pawn), actions)
        self.assertIn(SpellAction(bishop, spell, pawn), actions)

    def test_attack_multi_target(self):
        bishop = self.place_piece(Bishop, self.white, (4, 4))
        pawn1 = self.place_piece(Pawn, self.black, (3, 3))
        pawn2 = self.place_piece(Pawn, self.black, (6, 6))
        attack1 = self.add_attack(bishop, rng=1)
        attack2 = self.add_attack(bishop, name="Swipe", rng=2)

        actions = RulesEngine.get_valid_actions(bishop, self.board)
        self.assertIn(AttackAction(bishop, attack1, pawn1), actions)
        self.assertNotIn(AttackAction(bishop, attack1, pawn2), actions)
        self.assertIn(
            AttackAction(bishop, attack2, pawn2), actions
        )

    def test_spell_multi_target(self):
        bishop = self.place_piece(Bishop, self.white, (4, 4))
        pawn1 = self.place_piece(Pawn, self.black, (3, 3))
        pawn2 = self.place_piece(Pawn, self.black, (5, 5))
        spell = self.add_spell(bishop, rng=3)

        actions = RulesEngine.get_valid_actions(bishop, self.board)
        self.assertIn(SpellAction(bishop, spell, pawn1), actions)
        self.assertIn(SpellAction(bishop, spell, pawn2), actions)


if __name__ == "__main__":
    unittest.main()
