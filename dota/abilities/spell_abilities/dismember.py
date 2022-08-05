from dota.abilities.targeting_types.target_unit import TargetUnit


class DismemberAbility(TargetUnit):
    _BASE_MANA: int = 80
    _DEFAULT_NAME: str = "DISMEMBER"
    _MAX_LEVEL: int = 3
    _BASE_DAMAGE: int = 80
    _BASE_CAST_RANGE: int = 160
    _BASE_SEARCH_RADIUS = 5
    _DEFAULT_HOT_KEY = 'R'

    def __init__(self):
        super(DismemberAbility, self).__init__()
        self.mana = self._BASE_MANA
        self.name = self._DEFAULT_NAME
        self.max_level = self._MAX_LEVEL
        self.magic_type = "MAGICAL"
        self.cast_range = self._BASE_CAST_RANGE
        self.search_radius = self._BASE_SEARCH_RADIUS
        self.hot_key = self._DEFAULT_HOT_KEY
        self.base_damage = self._BASE_DAMAGE

    def level_up(self):
        if self.level < self._MAX_LEVEL:
            super(DismemberAbility, self).level_up()
            self.mana += self.mana * 0.2

