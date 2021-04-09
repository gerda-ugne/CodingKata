from random import randint


class Character:

    def __init__(self, id, health=1000, level=1, alive=True, stamina=100, mana=20):
        self.health = health
        self.level = level
        self.alive = alive
        self.experience = 0
        self.stamina = stamina
        self.id = id
        self.factions = []
        self.mana = mana
        self.weapon = None

######################################
    def join_faction(self, faction):
        if faction not in self.factions:
            self.factions.append(faction)

    def leave_faction(self, faction):
        if faction in self.factions:
            self.factions.remove(faction)

    def is_ally(self, c):
        return len(set(self.factions).intersection(c.factions)) != 0

    def dead(self):
        if self.health == 0:
            self.alive = False

    def heal(self, c):
        self.dead()
        if ((self.id == c.id) or self.is_ally(c)) and self.alive and self.health < 1000 and self.mana >= 10:
            self.health += 500
            self.mana -= 10
            if self.health > 1000:
                self.health = 1000
            return True
        return False

    def heal_self(self):
        return self.heal(self)
#############################################

    def deal_damage(self, enemy):
        if self == enemy:
            return False
        if self.stamina < 10:
            return False
        if not enemy.alive:
            return False

        #damage = randint(1, 100)
        damage = 50
        if self.weapon is not None:
            damage += self.weapon.attack_value

        self.stamina -= 10
        enemy.health -= damage
        if enemy.health <= 0:
            enemy.health = 0
            enemy.alive = False

        return True

    def add_experience(self, experience_points):
        requirements = pow(self.level, 2) * 10
        """We have the requirements.
        First see how many points we need to the next level."""
        points_to_next_level = requirements - self.experience

        if experience_points >= points_to_next_level:
            experience_points -= points_to_next_level
        else:
            self.experience += experience_points
            return

        while experience_points >= 0:
            self.experience += points_to_next_level
            self.experience = 0
            self.level += 1

            requirements = pow(self.level, 2) * 10
            points_to_next_level = requirements - self.experience
            if experience_points >= points_to_next_level:
                experience_points -= points_to_next_level
            else:
                self.experience += experience_points
                return

    def increment_stamina(self):
        self.stamina += 5
        if self.stamina > 100:
            self.stamina = 100

    def equip(self, weapon):
        if weapon.level_req <= self.level:

            if self.weapon:
                self.weapon.equipped = False
                self.weapon = None

            self.weapon = weapon
            weapon.equipped = True
            return True
        else:
            return False

    def unequip(self, weapon):
        weapon.equipped = False
        player.weapon = None


class Weapon:
    def __init__(self, attack_value, level_req, equipped=False):
        self.attack_value = attack_value
        self.level_req = level_req
        self.equipped = equipped


if __name__ == '__main__':
    player = Character(1)
    enemy = Character(2)

    player.add_experience(200)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
