import random

from human_brain_optimizer.constants.death_cause import DeathCause
from human_brain_optimizer.constants.food import Food
from human_brain_optimizer.models.actions.base import BaseAction
from human_brain_optimizer.models.data.log_request import LogRequest
from human_brain_optimizer.models.logger.eat import EatLogger


class Eat(BaseAction):
    ACTION_NAME = 'eat'
    FOOD_POISONING_PROBABILITY = 5
    FOOD_ENERGY_VALUE = 12

    @classmethod
    def run(cls, human):
        if Food.COOKED_FOOD in human.inventory:
            return cls.eat(human, cooked=True)
        elif Food.RAW_FOOD in human.inventory:
            cls.food_poisoning_check(human)
            return cls.eat(human, cooked=False)

    @classmethod
    def eat(cls, human, cooked=False):
        target_food = Food.COOKED_FOOD if cooked else Food.RAW_FOOD
        log_requests = cls.generate_logs(target_food, human)
        human.remove_item(target_food)
        human.food_level += cls.FOOD_ENERGY_VALUE
        human.sanitize()
        return log_requests

    @classmethod
    def food_poisoning_check(cls, human):
        if random.randint(0, 99) < cls.FOOD_POISONING_PROBABILITY:
            human.death_cause = DeathCause.FOOD_POISONING.value
            human.dead = True

    @classmethod
    def generate_logs(cls, target_food, human):
        food_type_log = LogRequest(
            logger_name=cls.ACTION_NAME,
            log_type=EatLogger.FOOD_LOG_TYPE,
            log_value=target_food
        )
        hunger_log = LogRequest(
            logger_name=cls.ACTION_NAME,
            log_type=EatLogger.HUNGER_LOG_TYPE,
            log_value=human.hunger()
        )
        return [food_type_log, hunger_log]
