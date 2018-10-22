from enums.GameClasses import GameClasses
from enums.WeaponType import WeaponType
from enums import *


class Character:
    def __init__(self, character_name, character_class):
        self.character_class = character_class
        self.character_name = character_name
        self.character_inventory = []
        self.equipment = []
        self.equipment[2] = "hallo"

    def equip_item(self, item):
        pass


print(GameClasses.warrior.value[1])
c = Character("help", GameClasses.warrior)
