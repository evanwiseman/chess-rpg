import unittest

from src.game import Board, Move, MoveType, Rules, Team, Player
from src.entities.pieces import (
    Bishop, King, Knight, Pawn, Queen, Rook
)


def place(board: Board, player: Player, piece_cls: type, pos: tuple[int, int]):
    piece = piece_cls()
    player.add_piece(piece)
    board.add_entity(pos, piece)
    return piece


class TestRules(unittest.TestCase):
    def test_bishop_default(self):
        player = Player(Team.WHITE)
        board = Board()

        bishop = place(board, player, Bishop, (7, 2))
        valid_moves = Rules.get_valid_moves(bishop, board, player)

        self.assertIn(
            Move((7, 2), (2, 7), MoveType.MOVE, bishop),
            valid_moves
        )
        self.assertIn(
            Move((7, 2), (5, 0), MoveType.MOVE, bishop),
            valid_moves
        )

    def test_bishop_obstructed(self):
        player = Player(Team.WHITE)
        board = Board()

        bishop = place(board, player, Bishop, (7, 2))
        place(board, player, Pawn, (6, 3))
        place(board, player, Pawn, (6, 1))
        valid_moves = Rules.get_valid_moves(bishop, board, player)

        self.assertListEqual(valid_moves, [])

    def test_bishop_open(self):
        board = Board()
        player = Player(Team.WHITE)

        bishop = place(board, player, Bishop, (4, 4))
        valid_moves = Rules.get_valid_moves(bishop, board, player)

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
        player = Player(Team.WHITE)
        board = Board()

        knight = place(board, player, Knight, (7, 1))
        valid_moves = Rules.get_valid_moves(knight, board, player)

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
        player = Player(Team.WHITE)
        board = Board()

        knight = place(board, player, Knight, (7, 1))
        place(board, player, Pawn, (6, 3))
        place(board, player, Pawn, (5, 2))
        place(board, player, Pawn, (5, 0))
        valid_moves = Rules.get_valid_moves(knight, board, player)

        self.assertEqual(valid_moves, [])

    def test_knight_open(self):
        board = Board()
        player = Player(Team.WHITE)

        knight = place(board, player, Knight, (4, 4))
        valid_moves = Rules.get_valid_moves(knight, board, player)

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

    def test_queen_default(self):
        board = Board()
        player = Player(Team.WHITE)

        queen = place(board, player, Queen, (7, 4))
        valid_moves = Rules.get_valid_moves(queen, board, player)

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
        player = Player(Team.WHITE)

        queen = place(board, player, Queen, (7, 4))
        place(board, player, King, (7, 3))
        place(board, player, Pawn, (6, 4))
        place(board, player, Pawn, (6, 3))
        place(board, player, Pawn, (6, 5))
        place(board, player, Bishop, (7, 5))
        valid_moves = Rules.get_valid_moves(queen, board, player)

        self.assertListEqual(valid_moves, [])

    def test_queen_open(self):
        board = Board()
        player = Player(Team.WHITE)

        queen = place(board, player, Queen, (4, 4))
        valid_moves = Rules.get_valid_moves(queen, board, player)

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
        player = Player(Team.WHITE)

        rook = place(board, player, Rook, (7, 0))
        valid_moves = Rules.get_valid_moves(rook, board, player)

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
        player = Player(Team.WHITE)

        rook = place(board, player, Rook, (7, 0))
        place(board, player, Pawn, (6, 0))
        place(board, player, Knight, (7, 1))
        valid_moves = Rules.get_valid_moves(rook, board, player)

        self.assertListEqual(valid_moves, [])

    def test_rook_open(self):
        board = Board()
        player = Player(Team.WHITE)

        rook = place(board, player, Rook, (4, 4))
        valid_moves = Rules.get_valid_moves(rook, board, player)

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
