from typing import Dict, List, Optional, Tuple, TYPE_CHECKING
from .cell import Cell
if TYPE_CHECKING:
    from src.backend.entities import Entity
    from src.backend.items import Item
    from src.backend.entities.pieces import Piece


class Board:
    def __init__(self, rows: int = 8, cols: int = 8):
        self._rows = rows
        self._cols = cols
        self._grid: List[List[Cell]] = [
            [Cell() for _ in range(cols)] for _ in range(rows)
        ]
        self._id_location_map: Dict[int, Tuple[int, int]] = {}

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    def get_cell(self, pos: Tuple[int, int]) -> Cell:
        """
        Get the Cell at the given position

        Args:
            pos (Tuple[int, int]): Position to get Cell at

        Returns:
            Cell in _grid at pos
        """
        row, col = pos
        return self._grid[row][col]

    def is_in_bounds(self, pos: Tuple[int, int]):
        row, col = pos
        return (
           0 <= row and row < self._rows
           and 0 <= col and col < self._cols
        )

    # --- Piece Methods ---
    def place_piece(self, pos: Tuple[int, int], piece: 'Piece'):
        """
        Place a piece at the given position

        Args:
            pos (Tuple[int, int]): Position to place the piece
            piece (Piece): The piece to place
        """
        cell = self.get_cell(pos)
        if cell.has_piece():
            raise ValueError(f"Cell ({pos}) already has a piece")
        if piece.id in self._id_location_map:
            raise KeyError(f"Piece is already placed ID {piece.id}")
        cell.piece = piece
        self._id_location_map[piece.id] = pos

    def get_piece_at(self, pos: Tuple[int, int]) -> Optional['Piece']:
        """
        Return a piece at the given position or None.

        Args:
            pos (Tuple[int, int]): Position to search.

        Returns:
            Piece at pos or None
        """
        cell = self.get_cell(pos)
        return cell.piece

    def remove_piece(self, piece: 'Piece'):
        """
        Remove a piece from the grid

        Args:
            piece (Piece): The piece to remove
        """
        if piece.id not in self._id_location_map:
            raise KeyError(f"ID {piece.id} not found in map")
        pos = self._id_location_map.pop(piece.id)
        cell = self.get_cell(pos)
        cell.piece = None

    def remove_piece_at(self, pos: Tuple[int, int]):
        """
        Removes a piece from the grid if found at pos

        Args:
            pos (Tuple[int, int]): Position to remove piece at
        """
        cell = self.get_cell(pos)
        if not cell.has_piece():
            return
        if cell.piece.id not in self._id_location_map:
            raise KeyError(f"ID {cell.piece.id} not found in map")
        del self._id_location_map[cell.piece.id]
        cell.piece = None

    def move_piece(self, start: Tuple[int, int], end: Tuple[int, int]):
        """
        Moves a piece from a start position to an end position

        Args:
            start (Tuple[int, int]): The start position
            end (Tuple[int, int]): The end position

        Raises:
            ValueError: If start has no piece or end is already occupied
        """
        start_cell = self.get_cell(start)
        end_cell = self.get_cell(end)

        if not start_cell.has_piece():
            raise ValueError(f"No piece at {start}")
        if end_cell.has_piece():
            raise ValueError(f"Cell {end} already occupied")

        piece = start_cell.piece
        end_cell.piece = piece
        start_cell.piece = None
        self._id_location_map[piece.id] = end

    # --- Item Methods ---
    def place_item(self, pos: Tuple[int, int], item: 'Item'):
        """
        Place an item at the given position

        Args:
            pos (Tuple[int, int]): Position to place item at
            item: The item to place

        Raises:
            ValueError: If the cell already contains an item
        """
        cell = self.get_cell(pos)
        if cell.has_item():
            raise ValueError(f"Cell ({pos}) already has an item")
        cell.item = item
        self._id_location_map[item.id] = pos

    def get_item_at(self, pos: Tuple[int, int]) -> Optional['Item']:
        """
        Return a item at the given position or None.

        Args:
            pos (Tuple[int, int]): Position to search.

        Returns:
            Item at pos or None
        """
        cell = self.get_cell(pos)
        return cell.item

    def remove_item(self, item: 'Item'):
        """
        Remove an item from the grid

        Args:
            item (Item): The item to remove
        """
        if item.id not in self._id_location_map:
            raise KeyError(f"ID {item.id} not found in map")
        pos = self._id_location_map.pop(item.id)
        cell = self.get_cell(pos)
        cell.item = None

    def remove_item_at(self, pos: Tuple[int, int]):
        """
        Removes a item from the grid if found at pos

        Args:
            pos (Tuple[int, int]): Position to remove item at
        """
        cell = self.get_cell(pos)
        if not cell.has_item():
            return
        if cell.item.id not in self._id_location_map:
            raise KeyError(f"ID {cell.item.id} not found in map")
        del self._id_location_map[cell.item.id]
        cell.item = None

    # --- Entity/Cell Methods ---
    def get_entity_location(self, entity: 'Entity'):
        if entity.id not in self._id_location_map:
            raise KeyError(f"ID {entity.id} not found in map")
        return self._id_location_map[entity.id]

    def clear_cell(self, pos: Tuple[int, int]):
        cell = self.get_cell(pos)
        cell.clear()
