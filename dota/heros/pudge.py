from common.dot_dictionary import DotDict
from dota.magics.hook import HookMagic
from dota.heros._base import Hero


class Pudge(Hero):
    def __init__(self):
        super(Pudge, self).__init__()
        self.magics = DotDict({'hook': HookMagic()})
