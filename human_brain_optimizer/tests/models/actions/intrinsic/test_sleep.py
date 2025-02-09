import pytest

from human_brain_optimizer.models.actions.intrinsic.sleep import Sleep
from human_brain_optimizer.models.human import Human


@pytest.fixture
def human():
    human = Human()
    human.energy_level = 0
    return human

def test_sanitize():
    sleep = Sleep()
    try:
        sleep.sanitize()
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")

def test_first_sleep(human):
    Sleep.use(human)
    assert human.energy_level == 1
    assert human.last_action == Sleep.ACTION_NAME

def test_second_sleep(human):
    human.last_action = Sleep.ACTION_NAME
    Sleep.use(human)
    assert human.energy_level == 3
    assert human.last_action == Sleep.ACTION_NAME

def test_excess_sleep(human):
    human.energy_level = 25
    Sleep.use(human)
    assert human.energy_level == 25
    assert human.last_action == Sleep.ACTION_NAME
