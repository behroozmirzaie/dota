from dota.abilities.active_ability import ActiveAbility


class NoTarget(ActiveAbility):
    def __init__(self):
        super(NoTarget, self).__init__()
        self._mana = 0

    @property
    def cast_range(self):
        return self._mana

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value: int):
        self._mana = int(value)
