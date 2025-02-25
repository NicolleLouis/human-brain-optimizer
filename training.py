from human_brain_optimizer.models.data.brain_config_range import BrainConfigRange
from human_brain_optimizer.models.training import Training

training_config = [
    BrainConfigRange(
        brain_name='hunt',
        config_name='ratio_amount',
        value_range=[-100, -50, -150, -200, -250]
    ),
    BrainConfigRange(
        brain_name='hunt',
        config_name='flat_amount',
        value_range=[600, 625, 650, 675, 700, 725, 775,  750, 800]
    ),
]
Training(training_config).run()
