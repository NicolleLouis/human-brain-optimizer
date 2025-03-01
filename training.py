from human_brain_optimizer.models.data.brain_config_range import BrainConfigRange
from human_brain_optimizer.models.training import Training

training_config = [
    BrainConfigRange(
        brain_name='train',
        config_name='flat_amount',
        value_range=list(range(0, 1001, 50))
    ),
]
Training(training_config).run()
