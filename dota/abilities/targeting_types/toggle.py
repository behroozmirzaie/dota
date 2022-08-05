from dota.abilities.active_ability import ActiveAbility


class Toggle(ActiveAbility):

    def __init__(self):
        super(Toggle, self).__init__()
        self._mana: int = 0
        self._cast_range: int = 0
        self._hot_key: str = ''
        self._base_damage: int = 0

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, value: int):
        self._mana = int(value)

    @property
    def cast_range(self) -> int:
        return self._cast_range

    @cast_range.setter
    def cast_range(self, value: int):
        self._cast_range = int(value)

    @property
    def hot_key(self) -> str:
        return self._hot_key.lower()

    @hot_key.setter
    def hot_key(self, value: str):
        self._hot_key = str(value)

    @property
    def base_damage(self) -> int:
        return self._base_damage

    @base_damage.setter
    def base_damage(self, value: int):
        self._base_damage = int(value)
