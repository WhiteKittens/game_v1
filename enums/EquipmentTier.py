from enum import Enum


class EquipmentTier(Enum):
    """
    value: index, drop rate in %, multiplier brackets
    """
    tier_0 = 0, 0, (19, 21)
    tier_1 = 1, 3, (16, 18)
    tier_2 = 2, 7, (13, 15)
    tier_3 = 3, 10, (10, 12)
    tier_4 = 4, 15, (7, 9)
    tier_5 = 5, 25, (4, 6)
    tier_6 = 6, 40, (1, 3)
