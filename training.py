from human_brain_optimizer.models.data.brain_config_range import BrainConfigRange
from human_brain_optimizer.models.training import Training

training_config = [
    # BrainConfigRange(
    #     brain_name='sleep',
    #     config_name='ratio_amount',
    #     value_range=[5, 10, 15, 20, 25, 30, 35, 40, 60, 80, 100]
    # ),
    # BrainConfigRange(
    #     brain_name='sleep',
    #     config_name='flat_amount',
    #     value_range=[0, 10, 20, 30, 40, 50]
    # ),
    BrainConfigRange(
        brain_name='sleep',
        config_name='already_asleep_bonus',
        value_range=[400, 425, 450, 475, 500, 525, 550, 575, 600]
    ),
]
Training(training_config).run()
