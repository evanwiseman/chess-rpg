from typing import List, Optional

from .constants import BOARD_ROW_SIZE, BOARD_COL_SIZE
from .pieces import Piece


class Board:
    def __init__(self, rows: int = BOARD_ROW_SIZE, cols: int = BOARD_COL_SIZE):
        self._rows = rows
        self._cols = cols
        self._board: List[List[Optional[Piece]]] = [
            [None for col in range(cols)] for row in range(rows)
        ]
