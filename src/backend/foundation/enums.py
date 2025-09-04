from enum import Enum


class ActionType(Enum):
    ATTACK = "attack"
    SPELL = "spell"
    ITEM = "item"
    OTHER = "other"


class MoveType(Enum):
    MOVE = "move"
    SPECIAL = "special"


class Team(Enum):
    WHITE = "white",
    BLACK = "black"


class EquipmentSlot(Enum):
    HELMET = "helmet"
    ARMOR = "armor"
    GLOVES = "gloves"
    LEGS = "legs"
    BOOTS = "boots"
    RING = "ring"
    NECKLACE = "necklace"
