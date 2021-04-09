import unittest
from main import Character


class Testing(unittest.TestCase):

   def test_deal_damage(self):
       player = Character()
       enemy = Character()
       result = player.deal_damage(enemy)

    def test_add_experience_less_than_one_level(self):
        player = Character()
        player.add_experience(6)
        self.assertEqual(player.experience,6)