import pytest

from human_brain_optimizer.models.brains.specific.random import RandomSpecificBrain
from human_brain_optimizer.models.human import Human


@pytest.fixture
def human():
    return Human()

def test_finesse(human):
    assert 0 < RandomSpecificBrain(human).finesse() < 1000
