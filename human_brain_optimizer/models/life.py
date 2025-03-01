from human_brain_optimizer.exceptions.life import HumanNotDead, UnexpectedDeath
from human_brain_optimizer.models.actions.extrinsic.hunt import Hunt
from human_brain_optimizer.models.data.brain_config import BrainConfig
from human_brain_optimizer.models.human import Human
from human_brain_optimizer.models.logger.ability import AbilityLogger
from human_brain_optimizer.models.logger.action import ActionLogger
from human_brain_optimizer.models.logger.inventory import InventoryLogger


class Life:
    BASE_EXTRINSIC_ACTIONS = [
        Hunt,
    ]

    def __init__(self, brain_config: [BrainConfig] = None):
        self.human = Human(brain_config)
        self.add_extrinsic_actions()
        self.action_logger = ActionLogger()
        self.inventory_logger = InventoryLogger()
        self.ability_logger = AbilityLogger()

    def run(self):
        while self.human.dead is False:
            action, finesse = self.human.turn()
            self.action_logger.log(action_name=action, finesse=finesse)
            self.inventory_logger.log(len(self.human.inventory))
            self.ability_logger.log(
                log_type='by_age',
                log_value=self.human.dexterity,
                age=self.human.age,
            )
        self.ability_logger.log(
            log_type='end_of_life',
            log_value=self.human.dexterity
        )

    def add_extrinsic_actions(self):
        self.human.set_external_actions(self.BASE_EXTRINSIC_ACTIONS)

    def death_cause(self):
        if not self.human.dead:
            raise HumanNotDead

        if self.human.energy_level <= 0 and self.human.food_level <= 0:
            return 'Food & Energy'
        elif self.human.energy_level <= 0:
            return 'Energy'
        elif self.human.food_level <= 0:
            return 'Food'
        elif self.human.age > Human.AGE_LIMIT:
            return 'Old age'
        else:
            raise UnexpectedDeath
