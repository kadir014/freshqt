from enum import Enum, auto


class TweenRepeatMode(Enum):
    """
    Repeating mode for tweening animations.

    Fields
    ------
    NONE
        Do not repeat.
    LOOP
        Repeat by looping to start.
    BOUNCE
        Repeat and reverse at each loop.
    """
    
    NONE = auto()
    LOOP = auto()
    BOUNCE = auto()