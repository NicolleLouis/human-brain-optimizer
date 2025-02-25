import pytest

from unittest.mock import MagicMock

from human_brain_optimizer.models.human import Human


@pytest.fixture
def human():
    return Human()


def test_initial_conditions(human):
    assert human.food_level == Human.MAXIMUM_INDICATOR_LEVEL
    assert human.energy_level == Human.MAXIMUM_INDICATOR_LEVEL
    assert human.age == 0
    assert not human.dead


def test_turn_consequence(human):
    human.turn_consequence()
    assert human.food_level == Human.MAXIMUM_INDICATOR_LEVEL - 1
    assert human.energy_level == Human.MAXIMUM_INDICATOR_LEVEL - 1
    assert human.age == 1


def test_death_probability_both_defection(human):
    human.food_level = 0
    human.energy_level = 0
    death_count = 0
    for _ in range(1000):
        human.death_check()
        if human.dead:
            death_count += 1
        human.dead = False
    assert 600 > death_count > 400


def test_death_probability_single_defection(human):
    human.food_level = 10
    human.energy_level = 0
    death_count = 0
    for _ in range(1000):
        human.death_check()
        if human.dead:
            death_count += 1
        human.dead = False
    assert 150 > death_count > 50

def test_sanitize_no_change(human):
    valid_value = 10
    human.food_level = valid_value
    human.energy_level = valid_value
    human.sanitize()
    assert human.food_level == valid_value
    assert human.energy_level == valid_value


def test_sanitize_change(human):
    invalid_value = 30
    human.food_level = invalid_value
    human.energy_level = invalid_value
    human.sanitize()
    assert human.food_level == human.MAXIMUM_INDICATOR_LEVEL
    assert human.energy_level == human.MAXIMUM_INDICATOR_LEVEL

def test_choose_action(human):
    human.actions = ["best_action", "action_1", "action_2"]
    human.brain.finesse = MagicMock(
        side_effect=lambda action: {"best_action": 10, "action_1": 5, "action_2": 1}[action]
    )
    assert human.choose_action() == "best_action"

def test_turn(human):
    human.turn()
    assert human.age == 1

def test_add_item(human):
    assert len(human.inventory) == 0
    human.add_item(1)
    assert len(human.inventory) == 1

def test_add_item_fail_case(human):
    human.inventory = [1] * human.MAXIMUM_INVENTORY_SIZE
    assert len(human.inventory) == human.MAXIMUM_INVENTORY_SIZE
    human.add_item(1)
    assert len(human.inventory) == human.MAXIMUM_INVENTORY_SIZE

def test_remove_item(human):
    human.inventory = [1]
    human.remove_item(1)
    assert len(human.inventory) == 0

def test_set_external_actions(human):
    assert len(human.actions) == len(human.INTRINSIC_ACTIONS)
    human.set_external_actions(["action_1"])
    assert len(human.actions) == len(human.INTRINSIC_ACTIONS) + 1

def test_old_age_death(human):
    human.age = human.AGE_LIMIT + 1
    human.death_check()
    assert human.dead
