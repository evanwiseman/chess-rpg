from enum import Enum


class MovementType(Enum):
    FORWARD = "forward"
    BACKWARD = "backward"
    LEFT = "left"
    RIGHT = "right"
    DIAGONAL = "diagonal"
    L_SHAPE = "l shape"


class Stats:
    def __init__(
        self,
        hp: int,
        damage: int,
        movement_range: int | None,
        movement_types: set[MovementType]
    ):
        self.__hp = max(0, hp)
        self.__damage = max(0, damage)
        if movement_range is None or movement_range >= 0:
            self.__movement_range = movement_range
        else:
            self.__movement_range = 0
        self.movement_types = movement_types

    def __eq__(self, value: 'Stats'):
        return (
            self.hp == value.hp
            and self.damage == value.damage
            and self.movement_range == value.movement_range
            and self.movement_types == value.movement_types
        )

    def __repr__(self):
        return (
            f"Stats({self.__hp}, {self.__damage}, {self.__movement_range}, "
            + f"{self.__movement_types})"
        )

    @property
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, value: int) -> None:
        self.__hp = max(0, value)

    @property
    def damage(self) -> int:
        return self.__damage

    @damage.setter
    def damage(self, value: int) -> None:
        self.__damage = max(0, value)

    @property
    def movement_range(self) -> int:
        return self.__movement_range

    @movement_range.setter
    def movement_range(self, value: int | None) -> None:
        if value is None or value >= 0:
            self.__movement_range = value
        else:
            self.__movement_range = 0

    @property
    def movement_types(self) -> set[MovementType]:
        return self.__movement_types

    @movement_types.setter
    def movement_types(self, value: set[MovementType]) -> None:
        self.__movement_types = value
