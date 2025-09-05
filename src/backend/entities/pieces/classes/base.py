from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.backend.stats import StatsManager

class PieceClass:
    def __init__(
        self,
        name: str,
        base_stats: 'StatsManager',
        
    )