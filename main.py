from dota.heros.pudge import Pudge

pudge = Pudge()


print(f"pudge flesh heap level:{pudge.abilities.flesh_heap.level} base damage: {pudge.abilities.flesh_heap.level}")
print(f"pudge flesh heap level:{pudge.abilities.rot.level} base damage: {pudge.abilities.flesh_heap.level}")
print(f"pudge flesh heap level:{pudge.abilities.flesh_heap.level} base damage: {pudge.abilities.flesh_heap.level}")
pudge.abilities.flesh_heap.level_up()

