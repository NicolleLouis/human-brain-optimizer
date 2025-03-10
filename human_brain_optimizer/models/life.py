from human_brain_optimizer.exceptions.models.life import LoggerNotFound
from human_brain_optimizer.models.actions.extrinsic.cook import Cook
from human_brain_optimizer.models.actions.extrinsic.hunt import Hunt
from human_brain_optimizer.models.data.brain_config import BrainConfig
from human_brain_optimizer.models.data.log_request import LogRequest
from human_brain_optimizer.models.human import Human
from human_brain_optimizer.models.logger.ability import AbilityLogger
from human_brain_optimizer.models.logger.action import ActionLogger
from human_brain_optimizer.models.logger.eat import EatLogger
from human_brain_optimizer.models.logger.inventory import InventoryLogger
from human_brain_optimizer.services.inventory_service import InventoryService


class Life:
    BASE_EXTRINSIC_ACTIONS = [
        Hunt,
        Cook,
    ]

    def __init__(self, brain_config: [BrainConfig] = None):
        self.human = Human(brain_config)
        self.add_extrinsic_actions()
        self.action_logger = ActionLogger()
        self.inventory_logger = InventoryLogger()
        self.ability_logger = AbilityLogger()
        self.eat_logger = EatLogger()

    def run(self):
        while self.human.dead is False:
            action, finesse, log_requests = self.human.turn()
            self.turn_logging(action=action, finesse=finesse, log_requests=log_requests)
        self.ability_logger.log(
            log_type='end_of_life',
            log_value=self.human.dexterity
        )

    def add_extrinsic_actions(self):
        self.human.set_external_actions(self.BASE_EXTRINSIC_ACTIONS)

    def turn_logging(self, action, finesse, log_requests: [LogRequest]):
        if log_requests is not None:
            list(map(self.add_log, log_requests))
        self.action_logger.log(action_name=action, finesse=finesse)
        self.inventory_logger.log(
            log_type=InventoryLogger.INVENTORY_SIZE_TYPE,
            log_value=len(self.human.inventory)
        )
        self.inventory_logger.log(
            log_type=InventoryLogger.SPECIFIC_ITEM_TYPE,
            log_value=InventoryService.generate_condensed_format(self.human)
        )
        self.ability_logger.log(
            log_type='by_age',
            log_value=self.human.dexterity,
            age=self.human.age,
        )

    def find_logger(self, logger_name):
        config = {
            'eat': self.eat_logger,
            'action': self.action_logger,
        }
        if logger_name in config:
            return config[logger_name]
        else:
            raise LoggerNotFound(logger_name)

    def add_log(self, log_request: LogRequest):
        logger = self.find_logger(log_request.logger_name)
        logger.log(log_request.log_type, log_request.log_value)
