from enums.GameClasses import GameClasses
from enums.WeaponType import WeaponType
from enums.Stats import Stats
from enums.Attributes import Attributes
from model.Weapon import Weapon


class Character:
    AMOUNT_OF_EQUIPMENT_SLOTS = 5
    BASE_STATS = 5

    def __init__(self, character_name, character_class=GameClasses.warrior):
        self.character_class = character_class
        self.character_name = character_name
        self.character_inventory = list()
        self.character_full_stats = dict()
        self.equiped_items = []
        self.init_equipment_slots()
        self.init_stats()

    def init_equipment_slots(self):
        for equipment_slot in range(self.AMOUNT_OF_EQUIPMENT_SLOTS):
            self.equiped_items += [None]

    def add_to_inventory(self, item):
        self.character_inventory.append(item)

    def remove_from_inventory(self, item):
        self.character_inventory.remove(item)

    def equip_item(self, item):
        if item.get_equipment_type in WeaponType.get_two_handed_weapons():
            if self.equiped_items[1] is not None:
                self.character_inventory.append(self.equiped_items[1])
                self.equiped_items[1] = None

        if self.equiped_items[item.get_equipment_type().value[3]] is not None:
            self.character_inventory.append(self.equiped_items[item.get_equipment_type().value[3]])
        self.equiped_items[item.get_equipment_type().value[3]] = item
        self.recalculate_stats()

    def init_stats(self):
        for stat in list(Stats):
            self.character_full_stats[stat] = self.BASE_STATS
        for attribute in list(Attributes):
            self.character_full_stats[attribute] = 0

    def recalculate_stats(self):
        for item in self.equiped_items:
            if item is not None:
                for stat in item.get_stats_and_attr():
                    self.character_full_stats[stat] += item.get_stats_and_attr()[stat][1]


weapon = Weapon(False)
character = Character("my char")
character.add_to_inventory(weapon)
character.equip_item(weapon)
print(character.character_full_stats)
print(WeaponType.two_handed_sword)
