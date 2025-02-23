import pytest
from unittest.mock import MagicMock
from human_brain_optimizer.exceptions.models.logger import UnknownLoggerNameException
from human_brain_optimizer.models.logger.general.base import GlobalLogger


def test_receive_message_logger_exists():
    global_logger = GlobalLogger()
    global_logger.config['lifespan'].log = MagicMock()
    global_logger.receive_message('lifespan', log_type='lifespan', log_value=1)
    global_logger.config['lifespan'].log.assert_called_once()

def test_receive_message_logger_not_exists():
    global_logger = GlobalLogger()
    with pytest.raises(UnknownLoggerNameException):
        global_logger.receive_message('nonexistent_logger')
