import math
import random
from weapon import Weapon

class Character:
  def __init__(self, name: str, level: int, str: str, proficiencies: list[str]):
    self.name = name
    self.level = level
    self.str = str
    self.proficiencies = proficiencies
  
  def roll_attack(self, weapon: Weapon):
    result = random.randint(1, 20) + self.str
    if weapon.name in self.proficiencies or weapon.category in self.proficiencies:
      result += self.__proficiency_bonus()
    return result

  def roll_damage(self, weapon: Weapon):
    dice_rolls = weapon.damage.split("d")
    damage = self.str
    for i in range(int(dice_rolls[0])):
      damage += random.randint(1, int(dice_rolls[1]))
    return damage
  
  def __proficiency_bonus(self):
    return 1 + (math.ceil(self.level / 4))