from human_brain_optimizer.constants.death_cause import DeathCause
from human_brain_optimizer.exceptions.models.life import HumanNotDead, UnexpectedDeath
from human_brain_optimizer.models.human import Human


class DeathCauseService:
    @staticmethod
    def get_death_cause(human):
        if not human.dead:
            raise HumanNotDead

        if human.energy_level <= 0 and human.food_level <= 0:
            return DeathCause.HUNGER_AND_ENERGY.value
        elif human.energy_level <= 0:
            return DeathCause.ENERGY.value
        elif human.food_level <= 0:
            return DeathCause.HUNGER.value
        elif human.age > Human.AGE_LIMIT:
            return DeathCause.OLD_AGE.value
        else:
            raise UnexpectedDeath
