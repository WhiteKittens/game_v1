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
    value: index , possible stats, possible attributes
    """
    two_handed_sword = 0, MELEE, MELEE_ATTR
    one_handed_sword = 1, MELEE, MELEE_ATTR
    dagger = 2, MELEE, MELEE_ATTR
    staff = 3, MAGIC, MAGIC_ATTR
    fist_weapon = 4, MELEE, MELEE_ATTR
