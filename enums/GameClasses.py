from enum import Enum
from enums.WeaponType import WeaponType


class GameClasses(Enum):
    warrior = 0, (WeaponType.two_handed_sword, WeaponType.one_handed_sword, WeaponType.axe)
    maybe = 1, None
