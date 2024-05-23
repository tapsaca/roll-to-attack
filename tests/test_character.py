import unittest
from src.character import Character

class TestCharacter(unittest.TestCase):
    def test_ability_modifier(self):
        char1 = Character("Name", 1, 1, [])
        char2 = Character("Name", 1, 9, [])
        char3 = Character("Name", 1, 10, [])
        char4 = Character("Name", 1, 19, [])
        char5 = Character("Name", 1, 20, [])
        self.assertEqual(char1._Character__ability_modifier(char1.str), -5)
        self.assertEqual(char2._Character__ability_modifier(char2.str), -1)
        self.assertEqual(char3._Character__ability_modifier(char3.str), 0)
        self.assertEqual(char4._Character__ability_modifier(char4.str), 4)
        self.assertEqual(char5._Character__ability_modifier(char5.str), 5)

    def test_proficiency_bonus(self):
        char1 = Character("Name", 1, 10, [])
        char2 = Character("Name", 8, 10, [])
        char3 = Character("Name", 9, 10, [])
        char4 = Character("Name", 20, 10, [])
        self.assertEqual(char1._Character__proficiency_bonus(), 2)
        self.assertEqual(char2._Character__proficiency_bonus(), 3)
        self.assertEqual(char3._Character__proficiency_bonus(), 4)
        self.assertEqual(char4._Character__proficiency_bonus(), 6)

if __name__ == "__main__":
    unittest.main()