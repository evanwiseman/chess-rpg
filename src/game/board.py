from typing import Dict, List, Optional, Tuple

from src.actions import Move, MoveResult, MoveStatus, MoveType
from src.constants import BOARD_ROW_SIZE, BOARD_COL_SIZE
from src.entities import Entity


class Board:
    def __init__(self, rows=BOARD_ROW_SIZE, cols=BOARD_COL_SIZE):
        self._rows = rows
        self._cols = cols
        self._board: List[List[Optional[Entity]]] = [
            [None for _ in range(cols)] for _ in range(rows)
        ]
        self._id_location_map: Dict[int, Tuple[int, int]] = {}

    def __repr__(self):
        lines = []
        for row in range(len(self._board)):
            entities = []
            for col in range(len(self._board[0])):
                entities.append(f"{self._board[row][col]}")
            lines.append("[ " + ", ".join(entities) + " ]")
        return "\n".join(lines)

    @property
    def size(self):
        return (self._rows, self._cols)

    def add_entity(self, location: Tuple[int, int], entity: Entity):
        row, col = location
        if self._board[row][col] is not None:
            raise ValueError(
                "Error: (Board.add_entity)"
                f"location ({row},{col}) already occupied"
            )
        if entity.id in self._id_location_map:
            raise KeyError(
                "Error: (Board.add_entity)"
                f"entity {entity} already placed."
            )
        self._board[row][col] = entity
        self._id_location_map[entity.id] = (row, col)

    def remove_entity_at(self, location: Tuple[int, int]) -> Entity:
        row, col = location
        entity = self._board[row][col]
        if not entity:
            raise ValueError(
                "Error: (Board.remove_entity_at)"
                f"no entity found at {location}."
            )
        self._board[row][col] = None
        if entity.id not in self._id_location_map:
            raise KeyError(
                "Error: (Board.remove_entity_at)"
                f"couldn't resolve entity id {entity.id}."
            )
        del self._id_location_map[entity.id]
        return entity

    def remove_entity(self, entity: Entity) -> Entity:
        self.remove_entity_by_id(entity.id)

    def remove_entity_by_id(self, id: int) -> Entity:
        if id not in self._id_location_map:
            raise KeyError(
                f"Error: (Board.remove_entity_by_id)"
                f"Invalid id {id}."
            )
        row, col = self._id_location_map[id]
        del self._id_location_map[id]

        entity = self._board[row][col]
        if not entity:
            raise ValueError(
                "Error: (Board.remove_entity_by_id)"
                f"no entity found at {(row, col)}"
            )
        self._board[row][col] = None
        return entity

    def get_entity_at(self, location: Tuple[int, int]) -> Optional[Entity]:
        row, col = location
        return self._board[row][col]

    def get_entity_by_id(self, id: int) -> Optional[Entity]:
        if id not in self._id_location_map:
            return None
        row, col = self._id_location_map[id]
        entity = self._board[row][col]
        if not entity:
            return None
        return entity

    def get_entity_location(self, entity: Entity) -> Tuple[int, int]:
        if not Entity:
            return (-1, -1)

        id = entity.id
        if id not in self._id_location_map:
            return (-1, -1)
        return self._id_location_map[id]

    def is_in_bounds(self, location: Tuple[int, int]) -> bool:
        row, col = location
        return (
            0 <= row and row < self._rows
            and 0 <= col and col < self._cols
        )

    def apply_move(self, move: Move):
        actor = move.actor
        start = move.start
        end = move.end

        if move.move_type == MoveType.MOVE:
            if self.get_entity_at(end) is not None:
                raise ValueError(f"Target cell {end} is not empty")
            # Update board
            self._board[end[0]][end[1]] = actor
            self._board[start[0]][start[1]] = None
            # Update id map
            self._id_location_map[actor.id] = end

            return MoveResult(move, status=MoveStatus.COMPLETED, target=None)

        elif move.move_type == MoveType.ATTACK:
            if move.target is None:
                raise ValueError("Attack move requires a target")
            target = self.get_entity_at(end)
            if target != move.target:
                raise ValueError(f"Attack target mismatch at {end}")

            # Board doesn’t resolve damage, just validates.
            return MoveResult(move, status=MoveStatus.PENDING, target=target)

        elif move.move_type == MoveType.CASTLE:
            # Move king + rook here
            pass

        elif move.move_type == MoveType.SPECIAL:
            # Defer to higher-level game systems
            return {"special": True, "actor": actor, "target": move.target}

        else:
            raise ValueError(f"Unknown move type {move.move_type}")
