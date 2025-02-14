import random

from human_brain_optimizer.models.actions.intrinsic.eat import Eat
from human_brain_optimizer.models.actions.intrinsic.sleep import Sleep
from human_brain_optimizer.models.brains.general.v1 import BrainV1


class Human:
    MAXIMUM_INDICATOR_LEVEL = 24
    MAXIMUM_INVENTORY_SIZE = 10
    INTRINSIC_ACTIONS = [
        Sleep,
        Eat,
    ]

    def __init__(self):
        self.food_level = self.MAXIMUM_INDICATOR_LEVEL
        self.energy_level = self.MAXIMUM_INDICATOR_LEVEL
        self.age = 0
        self.dead = False
        self.last_action = None
        self.inventory = []
        self.brain = BrainV1(self)
        self.actions = self.INTRINSIC_ACTIONS.copy()

    def choose_action(self):
        best_action = max(self.actions, key=lambda action: self.brain.finesse(action))
        return best_action

    def turn(self):
        action = self.choose_action()
        action.use(self)
        self.turn_consequence()
        return action.ACTION_NAME

    def sanitize(self):
        self.food_level = min(self.food_level, self.MAXIMUM_INDICATOR_LEVEL)
        self.energy_level = min(self.energy_level, self.MAXIMUM_INDICATOR_LEVEL)

    def turn_consequence(self):
        self.food_level -= 1
        self.energy_level -= 1
        self.age += 1
        self.death_check()

    def death_check(self):
        base_death_probability = 0
        if self.energy_level <= 0 and self.food_level <= 0:
            base_death_probability = 50
        elif self.energy_level <= 0 or self.food_level <= 0:
            base_death_probability = 10

        death_probability = base_death_probability
        if self.energy_level <= 0:
            death_probability += -self.energy_level
        if self.food_level <= 0:
            death_probability += -self.food_level

        if random.randint(0, 99) < death_probability:
            self.dead = True

    def add_item(self, item):
        if len(self.inventory) < self.MAXIMUM_INVENTORY_SIZE:
            self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def set_external_actions(self, external_actions):
        self.actions = self.INTRINSIC_ACTIONS.copy()
        self.actions.extend(external_actions)
