from src.backend.foundations.types import Vector2
from typing import Dict, Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from src.backend.entities import Entity


class BoardTile:
    """
    Represents a tile on a chess board. Can contain an entity.
    """
    def __init__(self, entity: Optional['Entity'] = None):
        """
        Create a board tile with an optional Entity attached.

        Args:
            entity (Entity, optional): An entity that occupies the Tile.
        """
        self.entity = entity

    def is_empty(self) -> bool:
        """
        Check if the tile contains any entity.

        Returns:
            bool: Returns True if entity is None otherwise False
        """
        return self.entity is None


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

    # --- Entity ---
    def contains_entity(self, entity: 'Entity'):
        return entity.id in self._id_position_map

    def get_entity_position(self, entity: 'Entity') -> Vector2:
        """
        Get the position on the board of an Entity.

        Args:
            entity (Entity): The entity to find.

        Returns:
            Vector2: The position of the entity on the board.
        """
        if entity.id not in self._id_position_map:
            raise KeyError(f"Entity {entity} is not on the board.")
        return self._id_position_map[entity.id]

    def get_entity_at(self, position: Vector2) -> Optional['Entity']:
        """
        Get the entity at a given position.

        Args:
            position (Vector2): The position to get the entity at.

        Returns:
            Optional[Entity]: The entity at a position or None.
        """
        tile = self._get_tile(position)
        return tile.entity

    def place_entity(self, entity: 'Entity', position: Vector2):
        """
        Place an entity on the board at a given location.

        Args:
            entity (Entity): The entity to place.
            position (Vector2): The position to place the entity.

        Raises:
            KeyError: If the piece is already on the board.
            ValueError: If a piece is already occupying the tile.
        """
        if self.contains_entity(entity):
            raise KeyError(f"Entity {entity} is already on the board.")

        tile = self._get_tile(position)
        if not tile.is_empty():
            raise ValueError(f"Position {position} is already occupied.")

        # Place the entity on the tile and update id position map
        tile.entity = entity
        self._id_position_map[entity.id] = position

    def move_entity(self, entity: 'Entity', new_position: Vector2):
        """
        Move an entity to a position.

        Args:
            entity (Entity): The entity to move.
            new_position (Vector2): The position to move the entity to.

        Raises:
            KeyError: If the entity is not on the board.
            ValueError: If an entity is already at the target position.
        """
        if not self.contains_entity(entity):
            raise KeyError(f"Entity {entity} is not on the board.")

        target = self.get_entity_at(new_position)
        if target is not None:
            raise ValueError(
                f"Position {new_position} is already occupied by {target}"
            )

        row, col = self.get_entity_position(entity)
        new_row, new_col = new_position

        # Set previous to new position
        self._grid[row][col].entity = None
        self._grid[new_row][new_col].entity = entity

        # Update id position map to new position
        self._id_position_map[entity.id] = new_position

    def remove_entity(self, entity: 'Entity') -> bool:
        """
        Remove an entity if it exists on the board.

        Args:
            entity (Entity): The entity to remove.

        Returns:
            bool: True if entity was removed, False otherwise.
        """
        if entity.id not in self._id_position_map:
            return False

        row, col = self.get_entity_position(entity)
        self._grid[row][col].entity = None
        del self._id_position_map[entity.id]
        return True

    def swap_entity(self, first: 'Entity', second: 'Entity'):
        """
        Swap two entities on the board.

        Args:
            first (Entity): The first entity to swap.
            second (Entity): The second entity to swap.

        Raises:
            KeyError: If the first entity is not on the board.
            KeyError: If the second entity is not ono the board.
        """
        if first.id not in self._id_position_map:
            raise KeyError(f"Entity {first} is not on the board.")
        if second.id not in self._id_position_map:
            raise KeyError(f"Entity {second} is not on the board.")

        first_row, first_col = self.get_entity_position(first)
        second_row, second_col = self.get_entity_position(second)

        # Swap the entities on respective tiles
        self._grid[first_row][first_col].entity = second
        self._grid[second_row][second_col].entity = first

        # Update the id position map to reflect the swap
        self._id_position_map[first.id] = (second_row, second_col)
        self._id_position_map[second.id] = (first_row, first_col)
