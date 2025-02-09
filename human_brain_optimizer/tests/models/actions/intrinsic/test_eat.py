import pytest

from human_brain_optimizer.models.actions.intrinsic.eat import Eat
from human_brain_optimizer.models.human import Human


@pytest.fixture
def human():
    human = Human()
    human.food_level = 0
    return human

def test_sanitize():
    sleep = Eat()
    try:
        sleep.sanitize()
    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")

def test_with_one_food(human):
    human.add_item('rabbit')
    Eat.use(human)
    assert human.food_level == 12
    assert human.last_action == Eat.ACTION_NAME

def test_with_no_food(human):
    Eat.use(human)
    assert human.food_level == 0
    assert human.last_action == Eat.ACTION_NAME

def test_with_multiple_food(human):
    human.add_item('rabbit')
    human.add_item('rabbit')
    Eat.use(human)
    assert human.food_level == 12
    assert human.last_action == Eat.ACTION_NAME
    assert len(human.inventory) == 1
