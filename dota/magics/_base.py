from abc import ABC


class AbstractMagic(ABC):
    @property
    def name(self):
        raise NotImplementedError

    @property
    def level(self):
        raise NotImplementedError

    @property
    def max_level(self):
        raise NotImplementedError


class BaseMagic(AbstractMagic):
    def __init__(self):
        self._level = 0
        self._max_level = 0
        self._name = None

    @property
    def level(self):
        return self._level

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.lower()

    @property
    def max_level(self):
        return self._max_level

    def level_up(self):
        print("you call this level up method")
        if self.level < self.max_level:
            self._level += 1


class ActiveMagic(BaseMagic):
    def __init__(self):
        super().__init__()
        self._mana: int = 0

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value: int):
        self._mana = value


class PassiveMagic(BaseMagic):
    ...
