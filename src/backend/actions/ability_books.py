from typing import Dict, Optional, Union
from .attack import Attack
from .spell import Spell


class AttackBook:
    def __init__(self):
        self._attacks: Dict[str, Attack] = {}

    def _normalize_attack(self, attack: Union[Attack, str]):
        if isinstance(attack, Attack):
            return attack.name.lower()
        elif isinstance(attack, str):
            return attack.lower()
        else:
            raise TypeError(
                f"Invalid spell type {type(attack).__name__}"
            )

    def add_attack(self, attack: Attack):
        key = self._normalize_attack(attack)
        if key in self._attacks:
            raise KeyError(f"Attack '{key}' already in AttackBook")
        self._attacks[key] = attack

    def remove_attack(self, attack: Union[Attack, str]):
        key = self._normalize_attack(attack)
        if key not in self._attacks:
            raise KeyError(f"Attack '{key}' not found in AttackBook")
        del self._attacks[key]

    def get_attack(self, name: str) -> Optional[Attack]:
        key = self._normalize_attack(name)
        return self._attacks.get(key)

    def all_attacks(self):
        return list(self._attacks.values())

    def __contains__(self, attack: Union[Attack, str]) -> bool:
        key = self._normalize_attack(attack)
        return key in self._attacks

    def __iter__(self):
        return iter(self._attacks.values())

    def __repr__(self):
        return f"<AttackBook {len(self._attacks)} attacks>"


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
