from typing import Dict, Optional, Union
from .attack import Attack


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
