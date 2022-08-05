from dota.abilities._base import BaseAbility


class ActiveAbility(BaseAbility):
    """
    Active abilities are targeted in different ways, depending on the effects of the ability.
    """

    def __init__(self):
        super().__init__()

    @property
    def mana(self):
        raise NotImplementedError

    @property
    def cast_range(self):
        raise NotImplementedError
