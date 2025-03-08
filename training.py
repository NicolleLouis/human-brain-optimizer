from human_brain_optimizer.models.data.brain_config_range import BrainConfigRange
from human_brain_optimizer.models.training import Training

training_config = [
    BrainConfigRange(
        brain_name='train',
        config_name='ratio_amount',
        value_range=list(range(-5, 5, 1))
    ),
]
Training(training_config).run()
