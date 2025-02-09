from human_brain_optimizer.models.logger.lifespan import LifespanLogger


def test_receive_lifespan_non_existent():
    logger = LifespanLogger()
    logger.log(10)
    assert logger.result_dict[10] == 1

def test_receive_lifespan_existent_key():
    logger = LifespanLogger()
    logger.result_dict[1] = 100
    logger.log(1)
    assert logger.result_dict[1] == 101
