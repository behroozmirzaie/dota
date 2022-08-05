from dota.abilities.targeting_types.toggle import Toggle


class RotAbility(Toggle):
    _BASE_MANA: int = 0
    _DEFAULT_NAME: str = "rot"
    _MAX_LEVEL: int = 4
    _BASE_DAMAGE: int = 30
    _BASE_CAST_RANGE: int = 1200
    _BASE_SEARCH_RADIUS = 250
    _DEFAULT_HOT_KEY = 'w'

    def __init__(self):
        super(RotAbility, self).__init__()
        self.mana = self._BASE_MANA
        self.name = self._DEFAULT_NAME
        self.max_level = self._MAX_LEVEL
        self.magic_type = "PURE"
        self.cast_range = self._BASE_CAST_RANGE
        self.search_radius = self._BASE_SEARCH_RADIUS
        self.hot_key = self._DEFAULT_HOT_KEY
        self.base_damage = self._BASE_DAMAGE

    def level_up(self):
        if self.level < self._MAX_LEVEL:
            super(RotAbility, self).level_up()
            self.base_damage += self.base_damage
