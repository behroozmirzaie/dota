class Hero:
    def __init__(self) -> None:
        self._name = None
        self._speed = 100
        self.abilities = {}

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.lower()
