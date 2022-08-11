from abc import ABC


class AbstractAbility(ABC):
    @property
    def name(self):
        raise NotImplementedError

    @property
    def level(self):
        raise NotImplementedError

    @property
    def max_level(self):
        raise NotImplementedError

    @property
    def magic_type(self):
        raise NotImplementedError


class BaseAbility(AbstractAbility):
    def __init__(self):
        self._level = 0
        self._max_level = 0
        self._name = None
        self._magic_type = None
        self._is_ultimate = False
        self._is_upgrade_by_aghanim = False

    @property
    def level(self) -> int:
        return self._level

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.lower()

    @property
    def max_level(self) -> int:
        return self._max_level

    @max_level.setter
    def max_level(self, value: int):
        self._max_level = value

    @property
    def magic_type(self) -> str:
        return self._magic_type

    @magic_type.setter
    def magic_type(self, value):
        self._magic_type = value

    @property
    def is_ultimate(self) -> bool:
        return self._is_ultimate

    @is_ultimate.setter
    def is_ultimate(self, value: bool):
        self._is_ultimate = value

    @property
    def is_upgrade_by_aghanim(self) -> bool:
        return self._is_upgrade_by_aghanim

    @is_upgrade_by_aghanim.setter
    def is_upgrade_by_aghanim(self, value: bool):
        self._is_upgrade_by_aghanim = value

    def level_up(self):
        if self.level < self.max_level:
            self._level += 1
