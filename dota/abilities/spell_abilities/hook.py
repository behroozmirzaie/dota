from dota.abilities.targeting_types.target_point import TargetPoint


class HookAbility(TargetPoint):
    _BASE_MANA: int = 100
    _DEFAULT_NAME: str = "HOOK"
    _MAX_LEVEL: int = 4
    _BASE_DAMAGE: int = 120
    _BASE_CAST_RANGE: int = 1200
    _BASE_SEARCH_RADIUS = 100
    _DEFAULT_HOT_KEY = 'Q'

    def __init__(self):
        super(HookAbility, self).__init__()
        self.mana = self._BASE_MANA
        self.name = self._DEFAULT_NAME
        self.max_level = self._MAX_LEVEL
        self.magic_type = "PURE"
        self.cast_range = self._BASE_CAST_RANGE
        self.search_radius = self._BASE_SEARCH_RADIUS
        self.hot_key = self._DEFAULT_HOT_KEY

    def level_up(self):
        if self.level < self._MAX_LEVEL:
            super(HookAbility, self).level_up()
            self.mana += self.mana * 0.3
