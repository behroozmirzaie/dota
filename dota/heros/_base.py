class Hero:
    _HERO_KIND = ['Intelligence', 'Strength', 'Agility']

    def __init__(self) -> None:
        self._name = None
        self._attack_speed = 100
        self._abilities = {}
        self._armor = 0
        self._intelligence = 0.0
        self._strength = 0.0
        self._agility = 0.0
        self._kind = None
        self._attack_range = 0
        self._projectile_attack = 0
        self._attack_damage = (0, 0)
        self._attack_rate = 0.0
        self._movement_speed = 0
        self._turn_speed = 0.0
        self._health = 0
        self._mana = 0
        self._health_regen = 0.0
        self._mana_regen = 0.0
        self._day_vision = 0
        self._night_vision = 0
        self._xp = 0
        self._level = 1
        self._collision_size = 0

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value.lower()

    @property
    def armor(self) -> int:
        return self._armor

    @armor.setter
    def armor(self, value: int):
        self._armor = value

    @property
    def intelligence(self) -> float:
        return self._intelligence

    @intelligence.setter
    def intelligence(self, value: float):
        self._intelligence = value

    @property
    def strength(self) -> float:
        return self._strength

    @strength.setter
    def strength(self, value: float):
        self._strength = value

    @property
    def agility(self) -> float:
        return self._agility

    @agility.setter
    def agility(self, value: float):
        self._agility = value

    @property
    def kind(self) -> str:
        return self._kind

    @kind.setter
    def kind(self, value: str):
        self._kind = value

    @property
    def attack_range(self) -> int:
        return self._attack_range

    @attack_range.setter
    def attack_range(self, value: int):
        self._attack_range = value

    @property
    def attack_damage(self) -> tuple:
        return self._attack_damage

    @attack_damage.setter
    def attack_damage(self, value: tuple):
        self._attack_damage = value

    @property
    def projectile_attack(self) -> int:
        return self._projectile_attack

    @projectile_attack.setter
    def projectile_attack(self, value: int):
        self._projectile_attack = value

    @property
    def attack_rate(self) -> float:
        return self._attack_rate

    @attack_rate.setter
    def attack_rate(self, value: float):
        self._attack_rate = value

    @property
    def movement_speed(self) -> int:
        return self._movement_speed

    @movement_speed.setter
    def movement_speed(self, value: int):
        self._movement_speed = value

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = value

    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, value: int):
        self._mana = value

    @property
    def health_regen(self) -> float:
        return self._health_regen

    @health_regen.setter
    def health_regen(self, value: float):
        self._health_regen = value

    @property
    def mana_regen(self) -> float:
        return self._mana_regen

    @mana_regen.setter
    def mana_regen(self, value: float):
        self._mana_regen = value

    @property
    def day_vision(self) -> int:
        return self._day_vision

    @day_vision.setter
    def day_vision(self, value: int):
        self._day_vision = value

    @property
    def night_vision(self) -> int:
        return self._night_vision

    @night_vision.setter
    def night_vision(self, value: int):
        self._night_vision = value

    @property
    def xp(self) -> int:
        return self._xp

    @xp.setter
    def xp(self, value: int):
        self._xp = value

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, value: int):
        self._level = value

    @property
    def attack_speed(self) -> int:
        return self._attack_speed

    @attack_speed.setter
    def attack_speed(self, value: int):
        self._attack_speed = value

    @property
    def turn_speed(self) -> float:
        return self._turn_speed

    @turn_speed.setter
    def turn_speed(self, value: float):
        self._turn_speed = value

    @property
    def collision_size(self) -> int:
        return self._collision_size

    @collision_size.setter
    def collision_size(self, value: int):
        self._collision_size = value

    def level_up(self):
        raise NotImplementedError
