from dota.heros._base import Hero


class Pudge(Hero):
    def __init__(self, abilities):
        super(Pudge, self).__init__()
        self.name = "PUDGE"
        self.abilities = abilities
