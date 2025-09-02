from typing import Dict, Optional
from .spell import Spell


class SpellBook:
    def __init__(self):
        self._spells: Dict[str, Spell] = {}

    def add_spell(self, spell: Spell):
        if spell.name in self._spells:
            raise KeyError(f"Spell '{spell.name}' already in SpellBook")
        self._spells[spell.name] = spell

    def remove_spell(self, name: str):
        if name not in self._spells:
            raise KeyError(f"Spell '{name}' not found in SpellBook")
        del self._spells[name]

    def get_spell(self, name: str) -> Optional[Spell]:
        return self._spells.get(name)

    def all_spells(self):
        return list(self._spells.values())

    def __contains__(self, name: str) -> bool:
        return name in self._spells

    def __iter__(self):
        return iter(self._spells.values())

    def __repr__(self):
        return f"<SpellBook {len(self._spells)} spells>"
