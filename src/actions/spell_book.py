from typing import Dict, Optional, Union
from .spell import Spell


class SpellBook:
    def __init__(self):
        self._spells: Dict[str, Spell] = {}

    def _normalize_spell(self, spell: Union[Spell, str]):
        if isinstance(spell, Spell):
            return spell.name.lower()
        elif isinstance(spell, str):
            return spell.lower()
        else:
            raise TypeError(
                f"Invalid spell type {type(spell).__name__}"
            )

    def add_spell(self, spell: Spell):
        key = self._normalize_spell(spell)
        if key in self._spells:
            raise KeyError(f"Spell '{key}' already in SpellBook")
        self._spells[key] = spell

    def remove_spell(self, spell: Union[Spell, str]):
        key = self._normalize_spell(spell)
        if key not in self._spells:
            raise KeyError(f"Spell '{key}' not found in SpellBook")
        del self._spells[key]

    def get_spell(self, name: str) -> Optional[Spell]:
        key = self._normalize_spell(name)
        return self._spells.get(key)

    def all_spells(self):
        return list(self._spells.values())

    def __contains__(self, spell: Union[Spell, str]) -> bool:
        key = self._normalize_spell(spell)
        return key in self._spells

    def __iter__(self):
        return iter(self._spells.values())

    def __repr__(self):
        return f"<SpellBook {len(self._spells)} spells>"
