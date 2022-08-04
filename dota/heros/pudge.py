from typing import List
from dota.magics.hook import HookMagic
from ._base import Hero
from common.dot_dictionary import  DotDict
class Pudge(Hero):
    def __init__(self):
        self.magics = DotDict({'hook': HookMagic()})


"""

dota
  +- heros
      + pudge
        + pudge.py
  + magics
    + hook.py



"""
