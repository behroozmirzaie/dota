from dota.abilities._base import BaseAbility


class AutoCastAbility(BaseAbility):
    def __init__(self):
        super(AutoCastAbility, self).__init__()
        self._mana: int = 0

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value: int):
        self._mana = int(value)
