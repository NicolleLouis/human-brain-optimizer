import pytest

from human_brain_optimizer.models.data.brain_config_range import BrainConfigRange
from human_brain_optimizer.services.brain_config_unpacker import BrainConfigUnpackerService


@pytest.fixture
def triple_range():
    return BrainConfigRange(
        brain_name="Lifespan",
        config_name="A",
        value_range=range(3),
    )

@pytest.fixture
def double_range():
    return BrainConfigRange(
        brain_name="Lifespan",
        config_name="A",
        value_range=range(2),
    )

@pytest.fixture
def single_range():
    return BrainConfigRange(
        brain_name="Action",
        config_name="B",
        value_range=range(1),
    )

def test_unpack_ranges_case_single(triple_range):
    iterables = list(BrainConfigUnpackerService.unpack_ranges([triple_range]))
    assert len(iterables) == 3


def test_unpack_ranges_case_double(triple_range, single_range):
    iterables = list(BrainConfigUnpackerService.unpack_ranges([triple_range, single_range]))
    assert len(iterables) == 3

def test_unpack_ranges_case_triple(triple_range, double_range, single_range):
    iterables = list(BrainConfigUnpackerService.unpack_ranges([triple_range, double_range, single_range]))
    assert len(iterables) == 6
