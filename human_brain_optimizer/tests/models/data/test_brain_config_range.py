import pytest

from human_brain_optimizer.models.data.brain_config import BrainConfig
from human_brain_optimizer.models.data.brain_config_range import BrainConfigRange


@pytest.fixture
def brain_config_range():
    return BrainConfigRange(
        brain_name="Lifespan",
        config_name="A",
        value_range=range(3),
    )


def test_convert_to_array(brain_config_range):
    result = brain_config_range.convert_to_array()
    assert len(result) == 3
    assert type(result[0]) == BrainConfig
