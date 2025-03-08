from human_brain_optimizer.models.data.brain_config_range import BrainConfigRange
from human_brain_optimizer.models.training import Training

training_config = [
    BrainConfigRange(
        brain_name='cook',
        config_name='flat_amount',
        value_range=list(range(300, 351, 20))
    ),
    BrainConfigRange(
        brain_name='train',
        config_name='flat_amount',
        value_range=list(range(420, 501, 20))
    ),
    BrainConfigRange(
        brain_name='train',
        config_name='ratio_amount',
        value_range=list(range(-100, 101, 50))
    ),
]
Training(training_config).run()
