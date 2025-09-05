from enum import Enum


class ActionResult(Enum):
    """Possible outcomes of action execution"""
    SUCCESS = "success"
    FAILED = "failed"
    BLOCKED = "blocked"
    INSUFFICIENT_RESOURCES = "insufficient_resources"
    INVALID_TARGET = "invalid_target"
    OUT_OF_RANGE = "out_of_range"


class ActionCategory(Enum):
    """High-level action categories"""
    MOVE = "move"
    ATTACK = "attack"
    SPELL = "spell"
    ABILITY = "ability"
    ITEM = "item"
    INTERACT = "interact"


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


class ModifierType(Enum):
    """
    Types of modifiers that can be applied to stats.
    """
    FLAT = "flat"
    PERCENTAGE = "percentage"
    MULTIPLIER = "multiplier"
