from human_brain_optimizer.models.data.brain_config_range import BrainConfigRange
from human_brain_optimizer.models.training import Training

training_config = [
    BrainConfigRange(
        brain_name='eat',
        config_name='flat_amount',
        value_range=[0, 250, 500, 750]
    ),
    BrainConfigRange(
        brain_name='eat',
        config_name='ratio_amount',
        value_range=[0, 25, 50, 75, 100]
    ),
]
Training(training_config).run()
