from random import randint


class Character:

    def __init__(self, weapon=None, health=1000, level=1, alive=True, stamina=100):
        self.health = health
        self.level = level
        self.alive = alive
        self.experience = 0
        self.stamina = stamina
        self.weapon = weapon

    def deal_damage(self, character):

        if self == character:
            return False
        if self.stamina < 10:
            return False

        damage = randint(1, 100)
        self.stamina -= 10

        character.health -= damage
        if character.health <= 0:
            character.health = 0
            character.alive = False

        return True

    def add_experience(self, experience_points):
        requirements = pow(2, self.level) * 10
        self.experience += experience_points
        if self.experience == requirements:
            self.experience = 0
            self.level = self.level + 1
        elif self.experience > requirements:
            experience_bank = self.experience - requirements
            self.experience = experience_bank
            self.level = self.level + 1

    def increment_stamina(self):
        self.stamina += 5
        if self.stamina > 100:
            self.stamina = 100


class Weapon:
    def __init__(self, attack_value, level_req, equipped=False):
        self.attack_value = attack_value
        self.level_req = level_req
        self.equipped = equipped

    def equip(self):
        self.equipped = True

    def unequip(self):
        self.equipped = False


if __name__ == '__main__':
    player = Character()
    enemy = Character()

    player.deal_damage(enemy)
    print("Health of Enemy:" + str(enemy.health))
    player.add_experience(20)
    print("Exp of player:" + str(player.experience))
    print("Level of player:" + str(player.level))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
