import pytest

from human_brain_optimizer.models.data.brain_config import BrainConfig


@pytest.fixture
def brain_config():
    return BrainConfig(
        brain_name='eat',
        config_name='flat_amount',
        value=0
    )

def test_str(brain_config):
    assert str(brain_config) == 'eat - flat_amount: 0'
