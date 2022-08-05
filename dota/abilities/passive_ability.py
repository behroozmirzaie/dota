from dota.abilities._base import BaseAbility


class PassiveAbility(BaseAbility):
    def __init__(self):
        super(PassiveAbility, self).__init__()
        self._radius: int = 0

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, value: int):
        self._radius = int(value)
