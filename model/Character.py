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
        self.equipped_items = []
        self.init_equipment_slots()
        self.init_stats()

    def init_equipment_slots(self):
        for equipment_slot in range(self.AMOUNT_OF_EQUIPMENT_SLOTS):
            self.equipped_items += [None]

    def add_to_inventory(self, item):
        self.character_inventory.append(item)

    def remove_from_inventory(self, item):
        self.character_inventory.remove(item)

    def equip_item(self, item):
        if item.get_equipment_type in WeaponType.get_two_handed_weapons():
            if self.equipped_items[1] is not None:
                self.character_inventory.append(self.equipped_items[1])
                self.equipped_items[1] = None

        if self.equipped_items[item.get_equipment_type().value[3]] is not None:
            self.character_inventory.append(self.equipped_items[item.get_equipment_type().value[3]])
        self.equipped_items[item.get_equipment_type().value[3]] = item
        self.recalculate_stats()

    def de_equip_item(self, item):
        self.equipped_items[item.get_equipment_type().value[3]] = None
        self.recalculate_stats()

    def init_stats(self):
        for stat in list(Stats):
            self.character_full_stats[stat] = self.BASE_STATS
        for attribute in list(Attributes):
            self.character_full_stats[attribute] = 0

    def recalculate_stats(self):
        self.init_stats()
        for item in self.equipped_items:
            if item is not None:
                for stat in item.get_stats_and_attr():
                    self.character_full_stats[stat] += item.get_stats_and_attr()[stat][1]
        return

    def print_character_stats(self):
        for stat in self.character_full_stats:
            if 0 < self.character_full_stats[stat]:
                print("%-28s  : %4d" % (stat.name.replace("_", " "), self.character_full_stats[stat]))
        return




weapon = Weapon(False)
character = Character("my char")
character.add_to_inventory(weapon)
character.equip_item(weapon)
character.print_character_stats()
character.de_equip_item(weapon)
character.print_character_stats()
