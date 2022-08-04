from common.dot_dictionary import DotDict
from dota.abilities.hook import HookAbility
from dota.heros._base import Hero


class Pudge(Hero):
    def __init__(self):
        super(Pudge, self).__init__()
        self.abilities = DotDict({'hook': HookAbility()})
        self.name = "PUDGE"
