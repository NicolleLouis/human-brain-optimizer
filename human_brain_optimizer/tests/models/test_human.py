import pytest

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
