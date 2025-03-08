import pytest

from human_brain_optimizer.exceptions.models.brain import UnknownConfigTypeException
from human_brain_optimizer.models.actions.intrinsic.train import Train
from human_brain_optimizer.models.brains.specific.train import TrainBrain
from human_brain_optimizer.models.human import Human


@pytest.fixture
def human():
    return Human()

@pytest.fixture
def brain(human):
    return TrainBrain(human)


def test_finesse(brain):
    brain.human.dexterity = TrainBrain.MAXIMUM_DEXTERITY
    assert brain.finesse() == 0

def test_set_config_flat_amount(brain):
    brain.set_config('flat_amount', 0)
    assert brain.flat_amount == 0

def test_set_config_false_value(brain):
    with pytest.raises(UnknownConfigTypeException):
        brain.set_config('wrong_param', 0)
