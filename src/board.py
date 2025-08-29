from typing import List, Optional

from .constants import BOARD_ROW_SIZE, BOARD_COL_SIZE
from src.entities import Entity


class Board:
    def __init__(self, rows=BOARD_ROW_SIZE, cols=BOARD_COL_SIZE):
        self._rows = rows
        self._cols = cols
        self._board: List[List[Optional[Entity]]] = [
            [None for _ in range(cols)] for _ in range(rows)
        ]

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

    def add_entity(self, location: tuple[int, int], entity: Entity):
        row, col = location
        if self._board[row][col] is not None:
            raise ValueError(f"Cell ({row},{col}) already occupied")
        self._board[row][col] = entity

    def remove_entity(self, location: tuple[int, int]):
        row, col = location
        self._board[row][col] = None

    def move_entity(self, start: tuple[int, int], end: tuple[int, int]):
        row_start, col_start = start
        row_end, col_end = end
        if self._board[row_end][col_end] is not None:
            raise ValueError(f"Target cell ({row_end},{col_end}) occupied")
        self._board[row_end][col_end] = self._board[row_start][col_start]
        self._board[row_start][col_start] = None

    def get_entity(self, location: tuple[int, int]) -> Optional[Entity]:
        row, col = location
        return self._board[row][col]
