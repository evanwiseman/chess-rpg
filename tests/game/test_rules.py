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
        valid_moves = Rules.get_valid_moves(
            bishop,
            board,
            player
        )
        self.assertIn(
            Move(
                start=(7, 2),
                end=(2, 7),
                move_type=MoveType.MOVE,
                actor=bishop
            ),
            valid_moves
        )
        self.assertIn(
            Move(
                start=(7, 2),
                end=(5, 0),
                move_type=MoveType.MOVE,
                actor=bishop
            ),
            valid_moves
        )

    def test_bishop_obstructed(self):
        player = Player(Team.WHITE)
        board = Board()

        bishop = place(board, player, Bishop, (7, 2))

        place(board, player, Pawn, (6, 3))
        place(board, player, Pawn, (6, 1))

        valid_moves = Rules.get_valid_moves(
            bishop,
            board,
            player
        )
        self.assertListEqual(valid_moves, [])

    def test_bishop_open(self):
        board = Board()
        player = Player(Team.WHITE)
        
    def test_knight_default(self):
        player = Player(Team.WHITE)
        board = Board()

        knight = place(board, player, Knight, (7, 1))
        valid_moves = Rules.get_valid_moves(
            knight,
            board,
            player
        )
        self.assertIn(
            Move(
                start=(7, 1),
                end=(6, 3),
                move_type=MoveType.MOVE,
                actor=knight
            ),
            valid_moves
        )
        self.assertIn(
            Move(
                start=(7, 1),
                end=(5, 2),
                move_type=MoveType.MOVE,
                actor=knight
            ),
            valid_moves
        )
        self.assertIn(
            Move(
                start=(7, 1),
                end=(5, 0),
                move_type=MoveType.MOVE,
                actor=knight
            ),
            valid_moves
        )

    def test_knight_obstructed(self):
        player = Player(Team.WHITE)
        board = Board()

        knight = place(board, player, Knight, (7, 1))
        place(board, player, Pawn, (6, 3))
        place(board, player, Pawn, (5, 2))
        place(board, player, Pawn, (5, 0))

        self.assertEqual(
            Rules.get_valid_moves(
                knight,
                board,
                player
            ),
            []
        )

    def test_queen_default(self):
        board = Board()
        player = Player(Team.WHITE)

        queen = place(board, player, Queen, (7, 4))
        valid_moves = Rules.get_valid_moves(
            queen,
            board,
            player
        )
        self.assertIn(
            Move(
                start=(7, 4),
                end=(0, 4),
                move_type=MoveType.MOVE,
                actor=queen
            ),
            valid_moves
        )
        self.assertIn(
            Move(
                start=(7, 4),
                end=(7, 7),
                move_type=MoveType.MOVE,
                actor=queen
            ),
            valid_moves
        )
        self.assertIn(
            Move(
                start=(7, 4),
                end=(7, 0),
                move_type=MoveType.MOVE,
                actor=queen
            ),
            valid_moves
        )
        self.assertIn(
            Move(
                start=(7, 4),
                end=(3, 0),
                move_type=MoveType.MOVE,
                actor=queen
            ),
            valid_moves
        )
        self.assertIn(
            Move(
                start=(7, 4),
                end=(4, 7),
                move_type=MoveType.MOVE,
                actor=queen
            ),
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
        self.assertListEqual(
            Rules.get_valid_moves(
                queen,
                board,
                player
            ),
            []
        )

    def test_rook_default(self):
        board = Board()
        player = Player(Team.WHITE)

        rook = place(board, player, Rook, (7, 0))
        valid_moves = Rules.get_valid_moves(
            rook,
            board,
            player
        )
        self.assertIn(
            Move(
                start=(7, 0),
                end=(0, 0),
                move_type=MoveType.MOVE,
                actor=rook
            ),
            valid_moves
        )
        self.assertIn(
            Move(
                start=(7, 0),
                end=(7, 7),
                move_type=MoveType.MOVE,
                actor=rook
            ),
            valid_moves
        )

    def test_rook_obstructed(self):
        board = Board()
        player = Player(Team.WHITE)

        rook = place(board, player, Rook, (7, 0))

        place(board, player, Pawn, (6, 0))
        place(board, player, Knight, (7, 1))
        self.assertListEqual(
            Rules.get_valid_moves(
                rook,
                board,
                player
            ),
            []
        )
