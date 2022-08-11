from common.dot_dictionary import DotDict
from dota.abilities.spell_abilities.dismember import DismemberAbility
from dota.abilities.spell_abilities.flesh_heap import FleshHeapAbility
from dota.abilities.spell_abilities.hook import HookAbility
from dota.abilities.spell_abilities.rot import RotAbility
from dota.heros.pudge import Pudge

heroes = DotDict(
    Pudge=Pudge(DotDict({'hook': HookAbility(), 'rot': RotAbility(), 'flesh_heap': FleshHeapAbility(),
                         'dismember': DismemberAbility()}))
)
