from human_brain_optimizer.models.logger.general.base import GlobalLogger
from human_brain_optimizer.models.logger.light_lifespan import LightLifespanLogger
from human_brain_optimizer.models.logger.training_result import TrainingResultLogger


class TrainingLogger(GlobalLogger):
    CONFIG = {
        'lifespan': LightLifespanLogger,
        'training': TrainingResultLogger
    }
