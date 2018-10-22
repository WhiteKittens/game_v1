from enum import Enum
from enums.Stats import Stats
from enums.Attributes import Attributes

STATS = [Stats.Stamina, Stats.Agility, Stats.Intelligence, Stats.Strength]
ATTR = [Attributes.armour, Attributes.energy_regen, Attributes.evasion_rating, Attributes.max_energy,
        Attributes.poison_resist, Attributes.elemental_resistance, Attributes.life]


class Rarity(Enum):
    """
    value: index , possible stats, possible attributes
    """
    helm = 0, STATS, ATTR, 2, "helm"
    body = 1, STATS, ATTR, 3, "body"
    legs = 2, STATS, ATTR, 4, "legs"
    shield = 3, STATS, ATTR, 1, "shield"
