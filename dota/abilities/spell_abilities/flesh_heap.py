from dota.abilities.passive_ability import PassiveAbility


class FleshHeapAbility(PassiveAbility):
    _DEFAULT_NAME: str = "flesh_heap"
    _MAX_LEVEL: int = 4
    _BASE_DAMAGE: int = 30
    _DEFAULT_HOT_KEY = 'e'

    def __init__(self):
        super(FleshHeapAbility, self).__init__()
        self.name = self._DEFAULT_NAME
        self.max_level = self._MAX_LEVEL
        self.hot_key = self._DEFAULT_HOT_KEY
        self._counter = 0

    def level_up(self):
        if self.level < self._MAX_LEVEL:
            super(FleshHeapAbility, self).level_up()

    def increase_flesh_heap(self):
        self._counter += 1

    @property
    def counter(self):
        return self._counter
