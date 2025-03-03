import pytest

from human_brain_optimizer.models.actions.extrinsic.hunt import Hunt
from human_brain_optimizer.models.human import Human


@pytest.fixture
def human():
    return Human()


def test_hunt_probability(human):
    successful_hunt_count = 0
    for _ in range(1000):
        Hunt.use(human)
        if len(human.inventory) > 0:
            successful_hunt_count += 1
        human.inventory = []
    assert 170 > successful_hunt_count > 100


def test_sanitize():
    sleep = Hunt()
    try:
        sleep.sanitize()
    except Exception as e:  # pragma: no cover
        pytest.fail(f"Unexpected exception raised: {e}")
