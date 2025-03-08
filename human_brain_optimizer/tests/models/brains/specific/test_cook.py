import pytest

from human_brain_optimizer.constants.food import Food
from human_brain_optimizer.exceptions.models.brain import UnknownConfigTypeException
from human_brain_optimizer.models.brains.specific.cook import CookBrain
from human_brain_optimizer.models.human import Human


@pytest.fixture
def human():
    human = Human()
    human.add_item(Food.RAW_FOOD)
    human.add_item(Food.COOKED_FOOD)
    return human

@pytest.fixture
def brain(human):
    return CookBrain(human)

def test_cooked_rabbit_collected(brain):
    assert brain.cooked_rabbit_collected() == 1
    brain.human.remove_item(Food.COOKED_FOOD)
    assert brain.cooked_rabbit_collected() == 0

def test_rabbit_collected(brain):
    assert brain.rabbit_collected() == 1
    brain.human.remove_item(Food.RAW_FOOD)
    assert brain.rabbit_collected() == 0

def test_set_config_case_success(brain):
    brain.set_config('flat_amount', 0)
    brain.set_config('uncooked_ratio_amount', 0)
    brain.set_config('cooked_ratio_amount', 0)
    assert brain.flat_amount == 0
    assert brain.cooked_ratio_amount == 0
    assert brain.uncooked_ratio_amount == 0

def test_set_config_case_error(brain):
    with pytest.raises(UnknownConfigTypeException):
        brain.set_config('wrong_param', 0)

def test_finesse_no_rabbit(brain):
    brain.human.remove_item(Food.RAW_FOOD)
    assert brain.finesse() == 0

def test_finesse(brain):
    assert brain.finesse() == brain.FLAT_AMOUNT + brain.COOKED_RATIO_AMOUNT + brain.UNCOOKED_RATIO_AMOUNT
