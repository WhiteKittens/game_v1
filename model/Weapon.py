from enums.Rarity import Rarity
from enums.WeaponType import WeaponType

import random


class Weapon:

    def __init__(self, full_import):
        self.rarity = ""
        self.equipment_name = ""
        self.equipment_type = ""
        self.equipment_stats = dict()
        self.equipment_attributes = dict()

        if full_import:
            return
        self.initialise_equipment()

    def initialise_equipment(self):
        self.initialise_rarity()
        self.initialise_type()
        self.initialise_name()

    def initialise_rarity(self):
        """
        initialises rarity by making a list of all rarities
        containing them once for each percentage of chance at getting them
        :return: None
        """
        rarity = ([Rarity.common] * Rarity.common.value[1]) + ([Rarity.uncommon] * Rarity.uncommon.value[1]) \
                 + ([Rarity.rare] * Rarity.rare.value[1]) + ([Rarity.legendary] * Rarity.legendary.value[1])

        self.rarity = random.choice(rarity)

    def initialise_type(self):
        self.equipment_type = random.choice(list(WeaponType))

    def initialise_name(self):
        self.equipment_name = self.equipment_type[3]

    def initialise_stats_and_attributes(self):
        pass


weapon = Weapon(False)
