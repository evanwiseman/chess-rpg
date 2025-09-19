from src.backend.foundations.types import Vector2
from typing import Dict, Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from src.backend.entities.pieces import Piece


class BoardTile:
    """
    Represents a tile on a chess board. Can contain a piece.
    """
    def __init__(self, piece: Optional['Piece'] = None):
        """
        Create a board tile with an optional piece attached.

        Args:
            piece (Piece, optional): A piece that occupies the Tile.
        """
        self.piece = piece

    def is_empty(self) -> bool:
        """
        Check if the tile contains any piece.

        Returns:
            bool: Returns True if piece is None otherwise False
        """
        return self.piece is None


class Board:
    """
    Represents a chess board. Comprised of tiles and id->position map for
    quick lookup.
    """
    def __init__(self, rows: int, cols: int):
        """
        Create a board with a size.

        Args:
            rows (int): Number of rows.
            cols (int): Number of cols.
        """
        self._rows = rows
        self._cols = cols
        self._grid = [[BoardTile() for _ in range(cols)] for _ in range(rows)]
        self._id_position_map: Dict[str, Vector2] = {}

    # --- Helpers ---
    def in_bounds(self, position: Vector2):
        """
        Check if a position is in bounds of the board.

        Args:
            pos (Vector2): The position to check.

        Returns:
            bool: Returns True if in bounds otherwise False
        """
        row, col = position
        return (
            0 <= row < self._rows
            and 0 <= col < self._cols
        )

    def _get_tile(self, position: Vector2) -> BoardTile:
        """
        Get the Tile on the board at a given position.

        Args:
            position (Vector2): The position to get from.

        Raises:
            IndexError: If the position is out of bounds.

        Returns:
            BoardTile: The tile at position.
        """
        if not self.in_bounds(position):
            raise IndexError(f"Position {position} is out of bounds.")
        row, col = position
        return self._grid[row][col]

    def get_size(self) -> Vector2:
        """
        Get the size of the board.

        Returns:
            Vector2: The size of the board (rows, cols)
        """
        return (self._rows, self._cols)

    # --- Piece ---
    def contains_piece(self, piece: 'Piece'):
        return piece.id in self._id_position_map

    def get_piece_position(self, piece: 'Piece') -> Vector2:
        """
        Get the position on the board of a piece.

        Args:
            piece (Piece): The piece to find.

        Returns:
            Vector2: The position of the piece on the board.
        """
        if piece.id not in self._id_position_map:
            raise KeyError(f"Piece {piece} is not on the board.")
        return self._id_position_map[piece.id]

    def get_piece_at(self, position: Vector2) -> Optional['Piece']:
        """
        Get the piece at a given position.

        Args:
            position (Vector2): The position to get the piece at.

        Returns:
            Optional[Piece]: The piece at a position or None.
        """
        tile = self._get_tile(position)
        return tile.piece

    def place_piece(self, piece: 'Piece', position: Vector2):
        """
        Place an piece on the board at a given location.

        Args:
            piece (Piece): The piece to place.
            position (Vector2): The position to place the piece.

        Raises:
            KeyError: If the piece is already on the board.
            ValueError: If a piece is already occupying the tile.
        """
        if self.contains_piece(piece):
            raise KeyError(f"Piece {piece} is already on the board.")

        tile = self._get_tile(position)
        if not tile.is_empty():
            raise ValueError(f"Position {position} is already occupied.")

        # Place the piece on the tile and update id position map
        tile.piece = piece
        self._id_position_map[piece.id] = position

    def move_piece(self, piece: 'Piece', new_position: Vector2):
        """
        Move an piece to a position.

        Args:
            piece (Piece): The piece to move.
            new_position (Vector2): The position to move the piece to.

        Raises:
            KeyError: If the piece is not on the board.
            ValueError: If an piece is already at the target position.
        """
        if not self.contains_piece(piece):
            raise KeyError(f"Piece {piece} is not on the board.")

        target = self.get_piece_at(new_position)
        if target is not None:
            raise ValueError(
                f"Position {new_position} is already occupied by {target}"
            )

        row, col = self.get_piece_position(piece)
        new_row, new_col = new_position

        # Set previous to new position
        self._grid[row][col].piece = None
        self._grid[new_row][new_col].piece = piece

        # Update id position map to new position
        self._id_position_map[piece.id] = new_position

    def remove_piece(self, piece: 'Piece') -> bool:
        """
        Remove an piece if it exists on the board.

        Args:
            piece (Piece): The piece to remove.

        Returns:
            bool: True if piece was removed, False otherwise.
        """
        if piece.id not in self._id_position_map:
            return False

        row, col = self.get_piece_position(piece)
        self._grid[row][col].piece = None
        del self._id_position_map[piece.id]
        return True

    def swap_piece(self, first: 'Piece', second: 'Piece'):
        """
        Swap two entities on the board.

        Args:
            first (Piece): The first piece to swap.
            second (Piece): The second piece to swap.

        Raises:
            KeyError: If the first piece is not on the board.
            KeyError: If the second piece is not ono the board.
        """
        if first.id not in self._id_position_map:
            raise KeyError(f"Piece {first} is not on the board.")
        if second.id not in self._id_position_map:
            raise KeyError(f"Piece {second} is not on the board.")

        first_row, first_col = self.get_piece_position(first)
        second_row, second_col = self.get_piece_position(second)

        # Swap the entities on respective tiles
        self._grid[first_row][first_col].piece = second
        self._grid[second_row][second_col].piece = first

        # Update the id position map to reflect the swap
        self._id_position_map[first.id] = (second_row, second_col)
        self._id_position_map[second.id] = (first_row, first_col)
