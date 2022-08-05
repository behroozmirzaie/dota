from dota.heros.pudge import Pudge

pudge = Pudge()

print(
    f"current pudge hook level is:{pudge.abilities.hook.level} and base damage is: {pudge.abilities.hook.base_damage}")
pudge.abilities.hook.level_up()
print(
    f"current pudge hook level is:{pudge.abilities.hook.level} and base damage is: {pudge.abilities.hook.base_damage}")
print(f"current pudge rot level is:{pudge.abilities.rot.level} and base damage is: {pudge.abilities.rot.base_damage}")
pudge.abilities.rot.level_up()
print(f"current pudge rot level is:{pudge.abilities.rot.level} and base damage is: {pudge.abilities.rot.base_damage}")
print(f"pudge flesh heap level:{pudge.abilities.flesh_heap.level} base damage: {pudge.abilities.flesh_heap.level}")
pudge.abilities.flesh_heap.level_up()
print(f"pudge flesh heap level:{pudge.abilities.flesh_heap.level} base damage: {pudge.abilities.flesh_heap.level}")
