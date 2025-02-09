import random


class Human:
    MAXIMUM_INDICATOR_LEVEL = 25

    def __init__(self):
        self.food_level = self.MAXIMUM_INDICATOR_LEVEL
        self.energy_level = self.MAXIMUM_INDICATOR_LEVEL
        self.age = 0
        self.dead = False

    def turn_consequence(self):
        self.food_level -= 1
        self.energy_level -= 1
        self.age += 1
        self.death_check()

    def death_check(self):
        death_probability = 0
        if self.energy_level <= 0 and self.food_level <= 0:
            death_probability = 50
        elif self.energy_level <= 0 or self.food_level <= 0:
            death_probability = 10
        if random.randint(0, 100) < death_probability:
            self.dead = True
