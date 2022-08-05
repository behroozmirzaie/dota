from common.dot_dictionary import DotDict
from dota.abilities.spell_abilities.hook import HookAbility
from dota.abilities.spell_abilities.rot import RotAbility
from dota.heros._base import Hero


class Pudge(Hero):
    def __init__(self):
        super(Pudge, self).__init__()
        self.abilities = DotDict({'hook': HookAbility(), 'rot': RotAbility()})
        self.name = "PUDGE"
