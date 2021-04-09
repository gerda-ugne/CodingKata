import unittest
from main import Character, Weapon


class Testing(unittest.TestCase):

    def test_deal_damage(self):
        player = Character(1)
        enemy = Character(2)

        original_health = enemy.health
        player.deal_damage(enemy)
        assert original_health - 50 == enemy.health
        assert enemy.health > 0

    def test_deal_damage_with_weapon(self):
        player = Character(1)
        player.equip(Weapon(20, 0))
        enemy = Character(2)

        original_health = enemy.health
        player.deal_damage(enemy)
        assert original_health - 70 == enemy.health
        assert enemy.health > 0

    def test_deal_too_much_damage(self):
        player = Character(1)
        enemy = Character(2)

        enemy.health = 20
        player.deal_damage(enemy)
        assert enemy.health == 0
        assert enemy.alive == False

    def test_self_damage(self):
        player = Character(1)
        original_health = player.health
        player.deal_damage(player)
        assert original_health == player.health

    def test_low_stamina_damage(self):
        player = Character(1)
        enemy = Character(2)

        player.stamina = 2
        original_health = enemy.health
        player.deal_damage(enemy)
        assert original_health == enemy.health

    def test_dead_enemy_damage(self):
        player = Character(1)
        enemy = Character(2)

        enemy.alive = False
        original_health = enemy.health
        player.deal_damage(enemy)
        assert original_health == enemy.health

    def test_increment_stamina(self):
        player = Character(1)
        player.stamina = 20
        player.increment_stamina()
        assert player.stamina == 25

    def test_increment_excessive_stamina(self):
        player = Character(1)
        player.increment_stamina()
        assert player.stamina == 100

    def test_add_experience_less_than_one_level(self):
        player = Character(1)
        player.add_experience(6)
        self.assertEqual(player.experience, 6)

    def test_decrement_stamina_when_attacking(self):
        player = Character(1)
        enemy = Character(2)

        original_stamina = player.stamina
        player.deal_damage(enemy)
        assert original_stamina - 10 == player.stamina

    def test_add_experience_of_one_level(self):
        player = Character(1)
        player.add_experience(10)
        self.assertEqual(player.experience, 0)
        self.assertEqual(player.level, 2)

    def test_add_more_experience_than_a_level(self):
        player = Character(1)
        player.add_experience(12)
        self.assertEqual(player.experience, 2)
        self.assertEqual(player.level, 2)

    def test_equip_weapon(self):
        player = Character(1)
        weapon = Weapon(0, 0)
        player.equip(weapon)

        assert player.weapon == weapon
        assert weapon.equipped == True

    def test_equip_too_high_level_weapon(self):
        player = Character(1)
        weapon = Weapon(0, 20)
        player.equip(weapon)

        assert player.weapon == None
        assert weapon.equipped == False

    #############################################
    def test_init_health(self):
        character = Character(1)
        assert character.health == 1000

    def test_init_level(self):
        character = Character(1)
        assert character.level == 1

    def test_init_alive(self):
        character = Character(1)
        assert character.alive

    def test_init_factions(self):
        character = Character(1)
        assert not character.factions

    def test_init_mana(self):
        character = Character(1)
        assert character.mana == 20

    def test_heal_self1(self):
        character = Character(1)
        character.heal_self()
        assert character.health == 1000

    def test_heal_self2(self):
        character = Character(1)
        character.heal_self()
        character.health = 100
        print(character.heal_self())
        assert character.health == 600

    def test_heal_self3(self):
        character = Character(1)
        character.health = 100
        character.heal_self()
        character.heal_self()
        assert character.health == 1000

    def test_heal(self):
        char1 = Character(1)
        char2 = Character(2)
        factions = ['f1', 'f2', 'f3', 'f4', 'f5']
        for x in factions[0:3]:
            char1.join_faction(x)
        for x in factions[2:5]:
            char2.join_faction(x)
        char1.health = 300
        assert char1.heal(char2)
