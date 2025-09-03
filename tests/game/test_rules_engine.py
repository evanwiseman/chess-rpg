import unittest

from src.actions import (
    Attack, AttackAction, Spell, SpellAction, Move, MoveType
)
from src.game import Board, RulesEngine, Team, Player
from src.entities.pieces import (
    Bishop, King, Knight, Pawn, Queen, Rook, Piece
)


def place(
    board: Board,
    player: Player,
    piece_cls: type,
    pos: tuple[int, int]
) -> Piece:
    piece = piece_cls()
    player.add_piece(piece)
    board.add_entity(pos, piece)
    return piece


class TestRulesMoves(unittest.TestCase):
    def test_bishop_default(self):
        player = Player("player", Team.WHITE)
        board = Board()

        bishop = place(board, player, Bishop, (7, 2))
        valid_moves = RulesEngine.get_valid_moves(bishop, board)

        self.assertIn(
            Move((7, 2), (2, 7), MoveType.MOVE, bishop),
            valid_moves
        )
        self.assertIn(
            Move((7, 2), (5, 0), MoveType.MOVE, bishop),
            valid_moves
        )

    def test_bishop_obstructed(self):
        player = Player("player", Team.WHITE)
        board = Board()

        bishop = place(board, player, Bishop, (7, 2))
        place(board, player, Pawn, (6, 3))
        place(board, player, Pawn, (6, 1))
        valid_moves = RulesEngine.get_valid_moves(bishop, board)

        self.assertListEqual(valid_moves, [])

    def test_bishop_open(self):
        board = Board()
        player = Player("player", Team.WHITE)

        bishop = place(board, player, Bishop, (4, 4))
        valid_moves = RulesEngine.get_valid_moves(bishop, board)

        self.assertIn(
            Move((4, 4), (0, 0), MoveType.MOVE, bishop),
            valid_moves
        )

        self.assertIn(
            Move((4, 4), (7, 7), MoveType.MOVE, bishop),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (1, 7), MoveType.MOVE, bishop),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (7, 1), MoveType.MOVE, bishop),
            valid_moves
        )

    def test_knight_default(self):
        player = Player("player", Team.WHITE)
        board = Board()

        knight = place(board, player, Knight, (7, 1))
        valid_moves = RulesEngine.get_valid_moves(knight, board)

        self.assertIn(
            Move((7, 1), (6, 3), MoveType.MOVE, knight),
            valid_moves
        )
        self.assertIn(
            Move((7, 1), (5, 2), MoveType.MOVE, knight),
            valid_moves
        )
        self.assertIn(
            Move((7, 1), (5, 0), MoveType.MOVE, knight),
            valid_moves
        )

    def test_knight_obstructed(self):
        player = Player("player", Team.WHITE)
        board = Board()

        knight = place(board, player, Knight, (7, 1))
        place(board, player, Pawn, (6, 3))
        place(board, player, Pawn, (5, 2))
        place(board, player, Pawn, (5, 0))
        valid_moves = RulesEngine.get_valid_moves(knight, board)

        self.assertEqual(valid_moves, [])

    def test_knight_open(self):
        board = Board()
        player = Player("player", Team.WHITE)

        knight = place(board, player, Knight, (4, 4))
        valid_moves = RulesEngine.get_valid_moves(knight, board)

        self.assertIn(
            Move((4, 4), (2, 3), MoveType.MOVE, knight),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (3, 2), MoveType.MOVE, knight),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (5, 6), MoveType.MOVE, knight),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (6, 5), MoveType.MOVE, knight),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (6, 3), MoveType.MOVE, knight),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (5, 2), MoveType.MOVE, knight),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (2, 5), MoveType.MOVE, knight),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (3, 6), MoveType.MOVE, knight),
            valid_moves
        )

    def test_pawn_default_first_move(self):
        player = Player("player", Team.WHITE)
        board = Board()

        pawn = place(board, player, Pawn, (6, 4))
        valid_moves = RulesEngine.get_valid_moves(pawn, board)

        self.assertIn(
            Move((6, 4), (5, 4), MoveType.MOVE, pawn),
            valid_moves
        )
        self.assertIn(
            Move((6, 4), (4, 4), MoveType.MOVE, pawn),
            valid_moves
        )

    def test_pawn_default_second_move(self):
        player = Player("player", Team.WHITE)
        board = Board()

        pawn = place(board, player, Pawn, (5, 4))
        pawn.set_moved(True)
        valid_moves = RulesEngine.get_valid_moves(pawn, board)

        self.assertIn(
            Move((5, 4), (4, 4), MoveType.MOVE, pawn),
            valid_moves
        )
        self.assertNotIn(
            Move((5, 4), (3, 4), MoveType.MOVE, pawn),
            valid_moves
        )

    def test_queen_default(self):
        board = Board()
        player = Player("player", Team.WHITE)

        queen = place(board, player, Queen, (7, 4))
        valid_moves = RulesEngine.get_valid_moves(queen, board)

        self.assertIn(
            Move((7, 4), (0, 4), MoveType.MOVE, queen),
            valid_moves
        )
        self.assertIn(
            Move((7, 4), (7, 7), MoveType.MOVE, queen),
            valid_moves
        )
        self.assertIn(
            Move((7, 4), (7, 0), MoveType.MOVE, queen),
            valid_moves
        )
        self.assertIn(
            Move((7, 4), (3, 0), MoveType.MOVE, queen),
            valid_moves
        )
        self.assertIn(
            Move((7, 4), (4, 7), MoveType.MOVE, queen),
            valid_moves
        )

    def test_queen_obstructed(self):
        board = Board()
        player = Player("player", Team.WHITE)

        queen = place(board, player, Queen, (7, 4))
        place(board, player, King, (7, 3))
        place(board, player, Pawn, (6, 4))
        place(board, player, Pawn, (6, 3))
        place(board, player, Pawn, (6, 5))
        place(board, player, Bishop, (7, 5))
        valid_moves = RulesEngine.get_valid_moves(queen, board)

        self.assertListEqual(valid_moves, [])

    def test_queen_open(self):
        board = Board()
        player = Player("player", Team.WHITE)

        queen = place(board, player, Queen, (4, 4))
        valid_moves = RulesEngine.get_valid_moves(queen, board)

        self.assertIn(
            Move((4, 4), (0, 0), MoveType.MOVE, queen),
            valid_moves
        )

        self.assertIn(
            Move((4, 4), (7, 7), MoveType.MOVE, queen),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (1, 7), MoveType.MOVE, queen),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (7, 1), MoveType.MOVE, queen),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (4, 0), MoveType.MOVE, queen),
            valid_moves
        )

        self.assertIn(
            Move((4, 4), (0, 4), MoveType.MOVE, queen),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (4, 7), MoveType.MOVE, queen),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (7, 4), MoveType.MOVE, queen),
            valid_moves
        )

    def test_rook_default(self):
        board = Board()
        player = Player("player", Team.WHITE)

        rook = place(board, player, Rook, (7, 0))
        valid_moves = RulesEngine.get_valid_moves(rook, board)

        self.assertIn(
            Move((7, 0), (0, 0), MoveType.MOVE, rook),
            valid_moves
        )
        self.assertIn(
            Move((7, 0), (7, 7), MoveType.MOVE, rook),
            valid_moves
        )

    def test_rook_obstructed(self):
        board = Board()
        player = Player("player", Team.WHITE)

        rook = place(board, player, Rook, (7, 0))
        place(board, player, Pawn, (6, 0))
        place(board, player, Knight, (7, 1))
        valid_moves = RulesEngine.get_valid_moves(rook, board)

        self.assertListEqual(valid_moves, [])

    def test_rook_open(self):
        board = Board()
        player = Player("player", Team.WHITE)

        rook = place(board, player, Rook, (4, 4))
        valid_moves = RulesEngine.get_valid_moves(rook, board)

        self.assertIn(
            Move((4, 4), (4, 0), MoveType.MOVE, rook),
            valid_moves
        )

        self.assertIn(
            Move((4, 4), (0, 4), MoveType.MOVE, rook),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (4, 7), MoveType.MOVE, rook),
            valid_moves
        )
        self.assertIn(
            Move((4, 4), (7, 4), MoveType.MOVE, rook),
            valid_moves
        )


class TestRulesActions(unittest.TestCase):
    def test_bishop_attack_one(self):
        board = Board()
        white = Player("white", Team.WHITE)
        black = Player("black", Team.BLACK)

        bishop: Bishop = place(board, white, Bishop, (4, 4))
        pawn: Pawn = place(board, black, Pawn, (3, 3))
        slash = Attack(
            name="Slash",
            description="",
            damage=10,
            stamina_cost=5,
            attack_range=1,
            cooldown=1,
        )
        bishop.attack_book.add_attack(
            slash
        )

        valid_actions = RulesEngine.get_valid_actions(bishop, board)
        self.assertIn(
            AttackAction(bishop, slash, pawn),
            valid_actions
        )

    def test_bishop_attack_multi(self):
        board = Board()
        white = Player("white", Team.WHITE)
        black = Player("black", Team.BLACK)

        bishop: Bishop = place(board, white, Bishop, (4, 4))
        pawn1: Pawn = place(board, black, Pawn, (3, 3))
        pawn2: Pawn = place(board, black, Pawn, (6, 6))
        slash = Attack(
            name="Slash",
            description="",
            damage=10,
            stamina_cost=5,
            attack_range=1,
            cooldown=1,
        )
        swipe = Attack(
            name="Swipe",
            description="",
            damage=10,
            stamina_cost=5,
            attack_range=2,
            cooldown=1,
        )
        bishop.attack_book.add_attack(slash)
        bishop.attack_book.add_attack(swipe)

        valid_actions = RulesEngine.get_valid_actions(bishop, board)

        self.assertIn(
            AttackAction(bishop, slash, pawn1),
            valid_actions
        )
        self.assertNotIn(
            AttackAction(bishop, slash, pawn2),
            valid_actions
        )

    def test_bishop_attack_multi_blocked(self):
        board = Board()
        white = Player("white", Team.WHITE)
        black = Player("black", Team.BLACK)

        bishop: Bishop = place(board, white, Bishop, (4, 4))
        pawn_blocked: Pawn = place(board, black, Pawn, (2, 2))
        pawn1: Pawn = place(board, black, Pawn, (3, 3))
        pawn2: Pawn = place(board, black, Pawn, (6, 6))
        slash = Attack(
            name="Slash",
            description="",
            damage=10,
            stamina_cost=5,
            attack_range=1,
            cooldown=1,
        )
        swipe = Attack(
            name="Swipe",
            description="",
            damage=10,
            stamina_cost=5,
            attack_range=2,
            cooldown=1,
        )
        bishop.attack_book.add_attack(slash)
        bishop.attack_book.add_attack(swipe)

        valid_actions = RulesEngine.get_valid_actions(bishop, board)

        self.assertIn(
            AttackAction(bishop, slash, pawn1),
            valid_actions
        )
        self.assertNotIn(
            AttackAction(bishop, slash, pawn2),
            valid_actions
        )
        self.assertNotIn(
            AttackAction(bishop, swipe, pawn_blocked),
            valid_actions
        )

    def test_bishop_spell_one(self):
        board = Board()
        white = Player("white", Team.WHITE)
        black = Player("black", Team.BLACK)

        bishop: Bishop = place(board, white, Bishop, (4, 4))
        pawn: Pawn = place(board, black, Pawn, (3, 3))

        magic_missile = Spell(
            name="Magic Missile",
            description="",
            damage=30,
            mana_cost=10,
            cast_range=3,
            cooldown=3
        )
        bishop.spell_book.add_spell(magic_missile)

        valid_actions = RulesEngine.get_valid_actions(bishop, board)

        self.assertIn(
            SpellAction(bishop, magic_missile, pawn),
            valid_actions
        )

    def test_bishop_spell_multi(self):
        board = Board()
        white = Player("white", Team.WHITE)
        black = Player("black", Team.BLACK)

        bishop: Bishop = place(board, white, Bishop, (4, 4))
        pawn1: Pawn = place(board, black, Pawn, (3, 3))
        pawn2: Pawn = place(board, black, Pawn, (5, 5))

        magic_missile = Spell(
            name="Magic Missile",
            description="",
            damage=30,
            mana_cost=10,
            cast_range=3,
            cooldown=3
        )
        bishop.spell_book.add_spell(magic_missile)

        valid_actions = RulesEngine.get_valid_actions(bishop, board)

        self.assertIn(
            SpellAction(bishop, magic_missile, pawn1),
            valid_actions
        )
        self.assertIn(
            SpellAction(bishop, magic_missile, pawn2),
            valid_actions
        )


if __name__ == "__main__":
    unittest.main()
