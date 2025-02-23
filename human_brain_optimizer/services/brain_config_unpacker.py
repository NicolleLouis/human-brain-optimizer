import itertools

from human_brain_optimizer.models.data.brain_config import BrainConfig
from human_brain_optimizer.models.data.brain_config_range import BrainConfigRange


class BrainConfigUnpackerService:
    @staticmethod
    def unpack_ranges(brain_ranges: [BrainConfigRange]) -> [BrainConfig]:
        iterables = [brain_range.convert_to_array() for brain_range in brain_ranges]
        return itertools.product(*iterables)
