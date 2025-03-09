from human_brain_optimizer.models.data.brain_config_range import BrainConfigRange
from human_brain_optimizer.models.training import Training

training_config = [
    BrainConfigRange(
        brain_name='eat',
        config_name='flat_amount',
        value_range=list(range(250, 326, 25))
    ),
    BrainConfigRange(
        brain_name='eat',
        config_name='ratio_amount',
        value_range=list(range(32, 38, 1))
    ),
    BrainConfigRange(
        brain_name='eat',
        config_name='uncooked_malus',
        value_range=list(range(100, 201, 50))
    ),
]
Training(training_config).run()
