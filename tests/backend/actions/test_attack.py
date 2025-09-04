import unittest
from src.backend.actions import Attack, Action
from src.backend.entities.base import Entity
from src.backend.foundation import ActionType


class TestAttack(unittest.TestCase):
    def test_create(self):
        attack = Attack(
            name="test",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )

        self.assertIsInstance(attack, Attack)
        self.assertEqual(attack.name, "test")
        self.assertEqual(attack.description, "")
        self.assertEqual(attack.damage, 0)
        self.assertEqual(attack.stamina_cost, 0)
        self.assertEqual(attack.attack_range, 0)
        self.assertEqual(attack.cooldown, 0)
        self.assertEqual(attack.area_of_effect, 0)

    def test_eq(self):
        attack1 = Attack(
            name="test",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )

        attack2 = Attack(
            name="test",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        self.assertEqual(attack1, attack2)


class TestAttackAction(unittest.TestCase):
    def test_create(self):
        attack = Attack(
            name="test",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        actor = Entity("actor")
        target = Entity("target")
        attack_action = Action(actor, attack, target, ActionType.ATTACK)

        self.assertIsInstance(attack_action, Action)
        self.assertEqual(attack_action.actor, actor)
        self.assertEqual(attack_action.payload, attack)
        self.assertEqual(attack_action.target, target)

    def test_eq(self):
        attack = Attack(
            name="test",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        actor = Entity("actor")
        target = Entity("target")
        attack_action1 = Action(actor, attack, target, ActionType.ATTACK)
        attack_action2 = Action(actor, attack, target, ActionType.ATTACK)

        self.assertEqual(attack_action1, attack_action2)


if __name__ == "__main__":
    unittest.main()
