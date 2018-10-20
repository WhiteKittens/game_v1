from enum import Enum


class Rarity(Enum):
    """
    value: index, drop rate in %,  #stats, #attributes
    """
    game_breaker = 0, 0, 0, 0
    common = 1, 50, 1, 2
    uncommon = 2, 25, 1, 3
    rare = 3, 20, 2, 3
    legendary = 4, 5, 2, 4
