from dota.abilities._base import ActiveAbility


class HookAbility(ActiveAbility):
    _BASE_MANA: int = 100
    _DEFAULT_NAME: str = "HOOK"
    _MAX_LEVEL: int = 4
    _BASE_DAMAGE: int = 120

    def __init__(self):
        super(HookAbility, self).__init__()
        self.mana = self._BASE_MANA
        self.name = self._DEFAULT_NAME
        self.max_level = self._MAX_LEVEL
        self.magic_type = "PURE"

    def level_up(self):
        if self.level < self._MAX_LEVEL:
            super(HookAbility, self).level_up()
            self.mana += self.mana * 0.3
