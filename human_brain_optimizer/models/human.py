import random

from human_brain_optimizer.models.actions.base import BaseAction
from human_brain_optimizer.models.actions.intrinsic.eat import Eat
from human_brain_optimizer.models.actions.intrinsic.sleep import Sleep
from human_brain_optimizer.models.actions.intrinsic.train import Train
from human_brain_optimizer.models.brains.general.v1 import BrainV1
from human_brain_optimizer.models.data.brain_config import BrainConfig


class Human:
    MAXIMUM_INDICATOR_LEVEL = 24
    MAXIMUM_INVENTORY_SIZE = 10
    INTRINSIC_ACTIONS: list[BaseAction] = [
        Sleep,
        Eat,
        Train,
    ]
    AGE_LIMIT = 1000

    def __init__(self, brain_config: [BrainConfig] = None):
        self.food_level = self.MAXIMUM_INDICATOR_LEVEL
        self.energy_level = self.MAXIMUM_INDICATOR_LEVEL
        self.age = 0
        self.dead = False
        self.last_action = None
        self.inventory = []
        self.dexterity = 0
        self.brain = BrainV1(self)
        self.actions: list[BaseAction] = self.INTRINSIC_ACTIONS.copy()
        self.death_cause = None
        if brain_config is not None:
            self.brain.set_configs(brain_config)

    def choose_action(self) -> tuple[BaseAction, int]:
        finesse_values = {action: self.brain.finesse(action) for action in self.actions}
        best_action = max(finesse_values, key=finesse_values.get)
        return best_action, finesse_values[best_action]

    def turn(self):
        action, finesse = self.choose_action()
        action.use(self)
        self.turn_consequence()
        return action.ACTION_NAME, finesse

    def sanitize(self):
        self.food_level = min(self.food_level, self.MAXIMUM_INDICATOR_LEVEL)
        self.energy_level = min(self.energy_level, self.MAXIMUM_INDICATOR_LEVEL)

    def turn_consequence(self):
        from human_brain_optimizer.services.death_cause import DeathCauseService

        self.food_level -= 1
        self.energy_level -= 1
        self.age += 1
        self.death_check()
        if self.dead and self.death_cause is None:
            self.death_cause = DeathCauseService.get_death_cause(self)

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

        if self.age > self.AGE_LIMIT:
            self.dead = True

    def add_item(self, item):
        if len(self.inventory) < self.MAXIMUM_INVENTORY_SIZE:
            self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def set_external_actions(self, external_actions):
        self.actions = self.INTRINSIC_ACTIONS.copy()
        self.actions.extend(external_actions)

    def gain_dexterity(self):
        self.dexterity += 1
