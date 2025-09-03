import unittest
from src.actions import Spell, SpellBook


class TestSpellBook(unittest.TestCase):
    def test_create(self):
        spell_book = SpellBook()
        self.assertIsInstance(spell_book, SpellBook)

    def test_add_spell(self):
        spell = Spell(
            name="test",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell_book = SpellBook()
        spell_book.add_spell(spell)
        self.assertIn(spell, spell_book.all_spells())

    def test_add_spell_multiple(self):
        spell1 = Spell(
            name="test1",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell2 = Spell(
            name="test2",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell3 = Spell(
            name="test3",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell_book = SpellBook()
        spell_book.add_spell(spell1)
        spell_book.add_spell(spell2)
        spell_book.add_spell(spell3)
        self.assertIn(spell1, spell_book.all_spells())
        self.assertIn(spell2, spell_book.all_spells())
        self.assertIn(spell3, spell_book.all_spells())

    def test_add_spell_duplicate(self):
        spell = Spell(
            name="test",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell_book = SpellBook()
        spell_book.add_spell(spell)
        self.assertIn(spell, spell_book.all_spells())
        self.assertRaises(KeyError, lambda: spell_book.add_spell(spell))

    def test_remove_spell(self):
        spell = Spell(
            name="test",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell_book = SpellBook()
        spell_book.add_spell(spell)
        self.assertIn(spell, spell_book.all_spells())
        spell_book.remove_spell(spell)
        self.assertNotIn(spell, spell_book.all_spells())

    def test_remove_spell_multiple(self):
        spell1 = Spell(
            name="test1",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell2 = Spell(
            name="test2",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell3 = Spell(
            name="test3",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell_book = SpellBook()
        spell_book.add_spell(spell1)
        spell_book.add_spell(spell2)
        spell_book.add_spell(spell3)
        self.assertIn(spell1, spell_book.all_spells())
        self.assertIn(spell2, spell_book.all_spells())
        self.assertIn(spell3, spell_book.all_spells())
        spell_book.remove_spell(spell1)
        spell_book.remove_spell(spell2)
        spell_book.remove_spell(spell3)
        self.assertNotIn(spell1, spell_book.all_spells())
        self.assertNotIn(spell2, spell_book.all_spells())
        self.assertNotIn(spell3, spell_book.all_spells())

    def test_remove_spell_missing(self):
        spell = Spell(
            name="test",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell_book = SpellBook()
        spell_book.add_spell(spell)
        self.assertIn(spell, spell_book.all_spells())
        spell_book.remove_spell(spell)
        self.assertNotIn(spell, spell_book.all_spells())
        self.assertRaises(KeyError, lambda: spell_book.remove_spell(spell))

    def test_remove_spell_by_name(self):
        spell = Spell(
            name="test",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell_book = SpellBook()
        spell_book.add_spell(spell)
        self.assertIn(spell, spell_book.all_spells())
        spell_book.remove_spell("test")
        self.assertNotIn(spell, spell_book.all_spells())

    def test_remove_spell_by_name_multiple(self):
        spell1 = Spell(
            name="test1",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell2 = Spell(
            name="test2",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell3 = Spell(
            name="test3",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell_book = SpellBook()
        spell_book.add_spell(spell1)
        spell_book.add_spell(spell2)
        spell_book.add_spell(spell3)
        self.assertIn(spell1, spell_book.all_spells())
        self.assertIn(spell2, spell_book.all_spells())
        self.assertIn(spell3, spell_book.all_spells())
        spell_book.remove_spell("test1")
        spell_book.remove_spell("test2")
        spell_book.remove_spell("test3")
        self.assertNotIn(spell1, spell_book.all_spells())
        self.assertNotIn(spell2, spell_book.all_spells())
        self.assertNotIn(spell3, spell_book.all_spells())

    def test_remove_spell_by_name_missing(self):
        spell = Spell(
            name="test",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell_book = SpellBook()
        spell_book.add_spell(spell)
        self.assertIn(spell, spell_book.all_spells())
        spell_book.remove_spell("test")
        self.assertNotIn(spell, spell_book.all_spells())
        self.assertRaises(KeyError, lambda: spell_book.remove_spell("test"))

    def test_get_spell(self):
        spell = Spell(
            name="test",
            description="",
            damage=0,
            mana_cost=0,
            cast_range=0,
            cooldown=0,
            area_of_effect=0,
        )
        spell_book = SpellBook()
        spell_book.add_spell(spell)
        self.assertEqual(spell, spell_book.get_spell("test"))


if __name__ == "__main__":
    unittest.main()
