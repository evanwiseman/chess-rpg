import unittest
from src.actions import Attack, AttackBook


class TestAttackBook(unittest.TestCase):
    def test_create(self):
        attack_book = AttackBook()
        self.assertIsInstance(attack_book, AttackBook)
        self.assertListEqual(attack_book.all_attacks(), [])

    def test_add_attack(self):
        attack_book = AttackBook()
        attack = Attack(
            name="test",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack_book.add_attack(attack)
        self.assertIn(attack, attack_book.all_attacks())

    def test_add_attack_multiple(self):
        attack_book = AttackBook()
        attack1 = Attack(
            name="test1",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack2 = Attack(
            name="test2",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack3 = Attack(
            name="test3",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack_book.add_attack(attack1)
        attack_book.add_attack(attack2)
        attack_book.add_attack(attack3)
        self.assertIn(attack1, attack_book.all_attacks())
        self.assertIn(attack2, attack_book.all_attacks())
        self.assertIn(attack3, attack_book.all_attacks())

    def test_add_duplicate(self):
        attack_book = AttackBook()
        attack = Attack(
            name="test",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack_book.add_attack(attack)
        self.assertRaises(KeyError, lambda: attack_book.add_attack(attack))

    def test_remove_attack(self):
        attack_book = AttackBook()
        attack = Attack(
            name="test",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack_book.add_attack(attack)
        self.assertIn(attack, attack_book.all_attacks())
        attack_book.remove_attack(attack)
        self.assertNotIn(attack, attack_book.all_attacks())

    def test_remove_attack_multiple(self):
        attack_book = AttackBook()
        attack1 = Attack(
            name="test1",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack2 = Attack(
            name="test2",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack3 = Attack(
            name="test3",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack_book.add_attack(attack1)
        attack_book.add_attack(attack2)
        attack_book.add_attack(attack3)
        self.assertIn(attack1, attack_book.all_attacks())
        self.assertIn(attack2, attack_book.all_attacks())
        self.assertIn(attack3, attack_book.all_attacks())
        attack_book.remove_attack(attack1)
        attack_book.remove_attack(attack2)
        attack_book.remove_attack(attack3)
        self.assertNotIn(attack1, attack_book.all_attacks())
        self.assertNotIn(attack2, attack_book.all_attacks())
        self.assertNotIn(attack3, attack_book.all_attacks())

    def test_remove_attack_missing(self):
        attack_book = AttackBook()
        attack = Attack(
            name="test",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack_book.add_attack(attack)
        self.assertIn(attack, attack_book.all_attacks())
        attack_book.remove_attack(attack)
        self.assertRaises(KeyError, lambda: attack_book.remove_attack(attack))

    def test_remove_attack_by_name(self):
        attack_book = AttackBook()
        attack = Attack(
            name="test",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack_book.add_attack(attack)
        self.assertIn(attack, attack_book.all_attacks())
        attack_book.remove_attack("test")
        self.assertNotIn(attack, attack_book.all_attacks())

    def test_remove_attack_by_name_multiple(self):
        attack_book = AttackBook()
        attack1 = Attack(
            name="test1",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack2 = Attack(
            name="test2",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack3 = Attack(
            name="test3",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack_book.add_attack(attack1)
        attack_book.add_attack(attack2)
        attack_book.add_attack(attack3)
        self.assertIn(attack1, attack_book.all_attacks())
        self.assertIn(attack2, attack_book.all_attacks())
        self.assertIn(attack3, attack_book.all_attacks())
        attack_book.remove_attack("test1")
        attack_book.remove_attack("test2")
        attack_book.remove_attack("test3")
        self.assertNotIn(attack1, attack_book.all_attacks())
        self.assertNotIn(attack2, attack_book.all_attacks())
        self.assertNotIn(attack3, attack_book.all_attacks())

    def test_remove_attack_by_name_missing(self):
        attack_book = AttackBook()
        attack = Attack(
            name="test",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack_book.add_attack(attack)
        self.assertIn(attack, attack_book.all_attacks())
        attack_book.remove_attack("test")
        self.assertRaises(
            KeyError, lambda: attack_book.remove_attack("test")
        )

    def test_get_attack(self):
        attack_book = AttackBook()
        attack = Attack(
            name="test",
            description="",
            damage=0,
            stamina_cost=0,
            attack_range=0,
            cooldown=0,
            area_of_effect=0
        )
        attack_book.add_attack(attack)
        self.assertEqual(attack, attack_book.get_attack("test"))


if __name__ == "__main__":
    unittest.main()
