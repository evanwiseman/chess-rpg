from typing import Dict, Optional
from .attack import Attack


class AttackBook:
    def __init__(self):
        self._attacks: Dict[str, Attack] = {}

    def add_attack(self, attack: Attack):
        if attack.name in self._attacks:
            raise KeyError(f"Attack '{attack.name}' already in AttackBook")
        self._attacks[attack.name] = attack

    def remove_attack(self, name: str):
        if name not in self._attacks:
            raise KeyError(f"Attack '{name}' not found in AttackBook")
        del self._attacks[name]

    def get_attack(self, name: str) -> Optional[Attack]:
        return self._attacks.get(name)

    def all_attacks(self):
        return list(self._attacks.values())

    def __contains__(self, name: str) -> bool:
        return name in self._attacks

    def __iter__(self):
        return iter(self._attacks.values())

    def __repr__(self):
        return f"<AttackBook {len(self._attacks)} attacks>"
