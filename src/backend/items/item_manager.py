from collections import defaultdict
from typing import Dict, List, Optional
from .item import Item
from .item_stack import ItemStack


class ItemManagerFullError(RuntimeError):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return super().__str__()


class ItemManager:
    def __init__(self, slots: int = 6):
        self._slots = slots
