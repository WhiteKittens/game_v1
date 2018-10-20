from interface import Interface, interface
from enums.Rarity import Rarity

import random


class Equipment(Interface):

    @interface.default
    def __init__(self, full_import):
        self.rarity = ""
        self.equipment_name = ""
        self.equipment_type = ""
        self.equipment_stats = dict()
        self.equipment_attributes = dict()

        if full_import:
            return
        self.initialise_equipment()

    @interface.default
    def initialise_equipment(self):
        self.initialise_rarity()
        self.initialise_name()

    @interface.default
    def initialise_rarity(self):
        rarity = ([Rarity.common] * Rarity.common.value[1]) + ([Rarity.uncommon] * Rarity.uncommon.value[1]) \
                 + ([Rarity.rare] * Rarity.rare.value[1]) + ([Rarity.legendary] * Rarity.legendary.value[1])

        self.rarity = random.choice(rarity)

    def initialise_name(self):
        pass

    def initialise_type(self):
        pass

    def initialise_stats_and_attributes(self):
        pass
