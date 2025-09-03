# src/board/cell.py
from typing import Optional
from src.entities.pieces import Piece
from src.entities.items import Item


class Cell:
    def __init__(self):
        self.piece: Optional[Piece] = None
        self.item: Optional[Item] = None

    def is_empty(self) -> bool:
        return (
            self.piece is None and self.item is None
        )

    def has_piece(self) -> bool:
        return self.piece is not None

    def has_item(self) -> bool:
        return self.item is not None

    def clear(self):
        self.piece = None
        self.item = None
