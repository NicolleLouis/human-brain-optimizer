from human_brain_optimizer.models.life import Life
from human_brain_optimizer.models.logger.main import MainLogger


class Experiment:
    LIFE_NUMBER = 10000

    def __init__(self):
        self.logger = MainLogger()

    def run(self):
        for _ in range(self.LIFE_NUMBER):
            life = Life()
            life.run()
            self.logger.receive_message(
                'lifespan',
                log_type='lifespan',
                log_value=life.human.age
            )
            self.logger.receive_message(
                'lifespan',
                log_type='death_cause',
                log_value=life.death_cause()
            )
            self.logger.merge_logger('action', life.action_logger)

        self.logger.save()
