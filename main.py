from dota.heros.pudge import Pudge

pudge = Pudge()

print(f"current pudge hook level {pudge.abilities.hook.level}")
pudge.abilities.hook.level_up()
print(f"current pudge hook level {pudge.abilities.hook.level}")
print(pudge.abilities.hook.cast_range)
print(pudge.abilities.hook.search_radius)
