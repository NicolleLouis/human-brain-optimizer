from enum import Enum


class DeathCause(Enum):
    ENERGY = 'Energy'
    FOOD_POISONING = 'Food poisoning'
    HUNGER = 'Hunger'
    HUNGER_AND_ENERGY = 'Hunger & Energy'
    OLD_AGE = 'Old age'
