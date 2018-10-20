from enum import Enum
from enums.Stats import Stats
from enums.Attributes import Attributes

STATS = [Stats.Stamina, Stats.Agility, Stats.Intelligence, Stats.Strength]
ATTR = [Attributes.armour, Attributes.energy_regen, Attributes.evasion_rating, Attributes.max_energy,
        Attributes.poison_resist, Attributes.elemental_resistance]


class Rarity(Enum):
    """
    value: index , possible stats, possible attributes
    """
    helm = 0, STATS, ATTR
    body = 1, STATS, ATTR
    legs = 2, STATS, ATTR
    shield = 3, STATS, ATTR
