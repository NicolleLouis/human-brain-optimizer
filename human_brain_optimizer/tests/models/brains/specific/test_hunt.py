import pytest

from human_brain_optimizer.models.brains.specific.hunt import HuntBrain
from human_brain_optimizer.models.human import Human


@pytest.fixture
def human():
    return Human()

def test_rabbit_collected_case_empty(human):
    assert HuntBrain(human).rabbit_collected() == 0

def test_rabbit_collected_case_one_rabbit(human):
    human.add_item('rabbit')
    assert HuntBrain(human).rabbit_collected() == 1

def test_rabbit_collected_case_multiple_rabbits(human):
    human.add_item('rabbit')
    human.add_item('rabbit')
    human.add_item('rabbit')
    assert HuntBrain(human).rabbit_collected() == 3
