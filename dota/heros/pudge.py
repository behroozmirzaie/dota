from common.dot_dictionary import DotDict
from dota.abilities.spell_abilities.hook import HookAbility
from dota.abilities.spell_abilities.rot import RotAbility
from dota.abilities.spell_abilities.flesh_heap import FleshHeapAbility
from dota.abilities.spell_abilities.dismember import DismemberAbility
from dota.heros._base import Hero


class Pudge(Hero):
    def __init__(self):
        super(Pudge, self).__init__()
        self.abilities = DotDict({'hook': HookAbility(), 'rot': RotAbility(), 'flesh_heap': FleshHeapAbility(),
                                  'dismember': DismemberAbility()})
        self.name = "PUDGE"

