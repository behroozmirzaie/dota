from dota.abilities.active_ability import ActiveAbility


class TargetPoint(ActiveAbility):

    def __init__(self):
        super(TargetPoint, self).__init__()
        self._mana: int = 0
        self._cast_range: int = 0
        self._search_radius: int = 0
        self._hot_key: str = ''

    @property
    def mana(self):
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
    def search_radius(self) -> int:
        return self._search_radius

    @search_radius.setter
    def search_radius(self, value: int):
        self._search_radius = int(value)

    @property
    def hot_key(self) -> str:
        return self._hot_key.lower()

    @hot_key.setter
    def hot_key(self, value: str):
        self._hot_key = str(value)
