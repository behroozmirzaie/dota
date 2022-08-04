from dota.heros.pudge import Pudge
from dota.abilities.hook import HookAbility

pudge = Pudge()

print(pudge.abilities.hook.mana)
print(pudge.abilities.hook.name)
print(pudge.abilities.hook.max_level)
print(f"current pudge hook level {pudge.abilities.hook.level}")
pudge.abilities.hook.level_up()
print(f"current pudge hook level {pudge.abilities.hook.level}")
pudge.abilities.hook.level_up()
print(f"current pudge hook level {pudge.abilities.hook.level}")
pudge.abilities.hook.level_up()
print(f"current pudge hook level {pudge.abilities.hook.level}")
pudge.abilities.hook.level_up()
print(f"current pudge hook level {pudge.abilities.hook.level}")
print(pudge.abilities.hook.mana)
print(pudge.abilities.hook.magic_type)
