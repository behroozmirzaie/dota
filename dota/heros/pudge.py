from dota.heros._base import Hero


class Pudge(Hero):

    def __init__(self, abilities):
        super(Pudge, self).__init__()
        self.name = "PUDGE"
        self.abilities = abilities
        self.mana = 267
        self.health = 700
        self.mana_regen = 0.8
        self.health_regen = 4.5
        self.attack_rate = 0.59
        self.attack_range = 175
        self.attack_damage = (45, 51)
        self.attack_speed = 100
        self.projectile_attack = 0
        self.turn_speed = 0.7
        self.day_vision = 700
        self.night_vision = 700
        self.collision_size = 24
        self.strength = 25
        self.agility = 14
        self.intelligence = 16

    def level_up(self):
        super(Pudge, self).level_up()
        self.agility += 1.4
        self.strength += 3
        self.intelligence += 1.8
        self.health += 56
        self.health_regen += 0.4

