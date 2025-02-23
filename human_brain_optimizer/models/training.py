from human_brain_optimizer.models.data.brain_config_range import BrainConfigRange
from human_brain_optimizer.models.life import Life
from human_brain_optimizer.models.logger.general.training import TrainingLogger
from human_brain_optimizer.services.brain_config_unpacker import BrainConfigUnpackerService


class Training:
    LIFE_NUMBER = 10000

    def __init__(self, training_config: [BrainConfigRange]):
        self.life_size = None
        self.experiments = None
        self.logger = TrainingLogger()
        self.training_config = training_config
        self.generate_experiments()
        self.generate_experiment_depth()

    def run(self):
        for brain_config in self.experiments:
            self.experiment(brain_config)
        self.logger.save(['training'])

    def generate_experiments(self):
        self.experiments = list(BrainConfigUnpackerService.unpack_ranges(self.training_config))

    def generate_experiment_depth(self):
        total_configuration = len(self.experiments)
        if total_configuration > 100:
            raise 'Too Large initial set'

        self.life_size = int(self.LIFE_NUMBER / total_configuration)

    def experiment(self, brain_config):
        for _ in range(self.life_size):
            life = Life(brain_config)
            life.run()
            self.logger.receive_message(
                'lifespan',
                log_type='lifespan',
                log_value=life.human.age
            )
        self.logger.save(['lifespan'])
        self.display_result(brain_config)
        self.logger.reset(['lifespan'])

    def display_result(self, brain_config):
        lifespan_logger = self.logger.get_logger('lifespan')
        average_lifespan = float(round(lifespan_logger.average_lifespan, 2))
        self.logger.receive_message(
            'training',
            result=average_lifespan,
            brain_config=brain_config
        )
