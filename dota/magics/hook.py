from dota.magics._base import ActiveMagic


class HookMagic(ActiveMagic):
    _DEFAULT_MANA: int = 100
    _DEFAULT_NAME: str = "HOOK"

    def __init__(self):
        super(HookMagic, self).__init__()
        self.mana = self._DEFAULT_MANA
        self.name = self._DEFAULT_NAME
