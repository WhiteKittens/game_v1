from enums.GameClasses import GameClasses
from enums.WeaponType import WeaponType
from model.Weapon import Weapon


class Character:
    AMOUNT_OF_EQUIPMENT_SLOTS = 5

    def __init__(self, character_name, character_class=GameClasses.warrior):
        self.character_class = character_class
        self.character_name = character_name
        self.character_inventory = []
        self.equiped_items = []
        self.init_equipment_slots()

    def init_equipment_slots(self):
        for equipment_slot in range(self.AMOUNT_OF_EQUIPMENT_SLOTS):
            self.equiped_items[equipment_slot] = None

    def equip_item(self, item):
        if item.get_equipment_type in WeaponType.get_two_handed_weapons(WeaponType):



print(WeaponType.two_handed_sword)
