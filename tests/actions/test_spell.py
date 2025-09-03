import unittest
from src.actions import Spell, SpellAction
from src.entities import Entity


class TestAttack(unittest.TestCase):
    def test_create(self):
        spell = Spell(
            name="test",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0
        )

        self.assertIsInstance(spell, Spell)
        self.assertEqual(spell.name, "test")
        self.assertEqual(spell.description, "")
        self.assertEqual(spell.damage, 0)
        self.assertEqual(spell.mana_cost, 0)
        self.assertEqual(spell.cooldown, 0)
        self.assertEqual(spell.cooldown, 0)
        self.assertEqual(spell.area_of_effect, 0)

    def test_eq(self):
        spell1 = Spell(
            name="test",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0
        )

        spell2 = Spell(
            name="test",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0
        )
        self.assertEqual(spell1, spell2)


class TestAttackAction(unittest.TestCase):
    def test_create(self):
        spell = Spell(
            name="test",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0
        )
        actor = Entity("actor")
        target = Entity("target")
        attack_action = SpellAction(actor, spell, target)

        self.assertIsInstance(attack_action, SpellAction)
        self.assertEqual(attack_action.actor, actor)
        self.assertEqual(attack_action.payload, spell)
        self.assertEqual(attack_action.target, target)

    def test_eq(self):
        spell = Spell(
            name="test",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0
        )
        actor = Entity("actor")
        target = Entity("target")
        attack_action1 = SpellAction(actor, spell, target)
        attack_action2 = SpellAction(actor, spell, target)

        self.assertEqual(attack_action1, attack_action2)


if __name__ == "__main__":
    unittest.main()
