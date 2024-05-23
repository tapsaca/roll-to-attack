import math
import random
from src.weapon import Weapon

class Character:
  def __init__(self, name: str, level: int, str: int, proficiencies: list[str]):
    self.name = name
    self.level = level
    self.str = str
    self.proficiencies = proficiencies
  
  def roll_attack(self, weapon: Weapon):
    result = random.randint(1, 20) + self.__ability_modifier(self.str)
    if weapon.name in self.proficiencies or weapon.category in self.proficiencies:
      result += self.__proficiency_bonus()
    return result

  def roll_damage(self, weapon: Weapon):
    rolls_and_die = weapon.damage.split("d")
    damage = self.__ability_modifier(self.str)
    for _ in range(int(rolls_and_die[0])):
      damage += random.randint(1, int(rolls_and_die[1]))
    return damage
  
  def __ability_modifier(self, ability_score: int):
    return math.floor((ability_score - 10) / 2)
  
  def __proficiency_bonus(self):
    return 1 + (math.ceil(self.level / 4))