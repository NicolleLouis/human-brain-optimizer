import pytest
from unittest.mock import MagicMock
from human_brain_optimizer.models.logger.main import MainLogger
from human_brain_optimizer.exceptions.models.logger import UnknownLoggerNameException

def test_receive_message_logger_exists():
    main_logger = MainLogger()
    main_logger.config['lifespan'].log = MagicMock()
    main_logger.receive_message('lifespan', 'Test message')
    main_logger.config['lifespan'].log.assert_called_once_with('Test message')

def test_receive_message_logger_not_exists():
    main_logger = MainLogger()
    with pytest.raises(UnknownLoggerNameException):
        main_logger.receive_message('nonexistent_logger', 'Test message')
