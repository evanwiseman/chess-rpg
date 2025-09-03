import unittest
from src.actions import Attack, AttackAction
from src.entities import Entity


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
        attack_action = AttackAction(actor, attack, target)

        self.assertIsInstance(attack_action, AttackAction)
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
        attack_action1 = AttackAction(actor, attack, target)
        attack_action2 = AttackAction(actor, attack, target)

        self.assertEqual(attack_action1, attack_action2)


if __name__ == "__main__":
    unittest.main()
