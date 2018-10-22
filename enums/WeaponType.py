from enum import Enum
from enums.Stats import Stats
from enums.Attributes import Attributes

MELEE = [Stats.Strength, Stats.Stamina, Stats.Agility]
MAGIC = [Stats.Stamina, Stats.Strength, Stats.Intelligence]

MELEE_ATTR = [Attributes.global_damage_multiplier, Attributes.poison, Attributes.critical_strike_chance,
              Attributes.critical_strike_multiplier, Attributes.life_steal, Attributes.elemental_conversion,
              Attributes.elemental_bonus]
MAGIC_ATTR = [Attributes.global_damage_multiplier, Attributes.poison, Attributes.critical_strike_chance,
              Attributes.critical_strike_multiplier, Attributes.life_steal, Attributes.elemental_conversion,
              Attributes.elemental_bonus]


class WeaponType(Enum):
    """
    value: index , possible stats, possible attributes, equipment slot ,name
    """
    two_handed_sword = 0, MELEE, MELEE_ATTR, 0, "sword"
    one_handed_sword = 1, MELEE, MELEE_ATTR, 0, "sword"
    dagger = 2, MELEE, MELEE_ATTR, 0, "dagger"
    staff = 3, MAGIC, MAGIC_ATTR, 0, "staff"
    fist_weapon = 4, MELEE, MELEE_ATTR, 0, "fist"
    axe = 5, MELEE, MELEE_ATTR, 0, "axe"
