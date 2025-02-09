from unittest.mock import MagicMock, patch

import pytest

from human_brain_optimizer.models.logger.lifespan import LifespanLogger


@pytest.fixture
def lifespan_logger():
    logger = LifespanLogger()
    logger.result_dict = {1: 10, 2: 20, 3: 30}
    return logger

def test_receive_lifespan_non_existent():
    logger = LifespanLogger()
    logger.log(10)
    assert logger.result_dict[10] == 1

def test_receive_lifespan_existent_key():
    logger = LifespanLogger()
    logger.result_dict[1] = 100
    logger.log(1)
    assert logger.result_dict[1] == 101

def test_enrich_dataframe(lifespan_logger):
    lifespan_logger.enrich_dataframe()
    df = lifespan_logger.df

    assert df is not None
    assert list(df['age']) == [1, 2, 3]
    assert list(df['death_count']) == [10, 20, 30]
    assert list(df['cumulative_deaths']) == [10, 30, 60]
    assert list(df['alive_before']) == [60, 50, 30]
    assert list(df['death_probability']) == [10/60, 20/50, 30/30]

def test_save_raw(lifespan_logger):
    mock_file = MagicMock()
    with patch('builtins.open', mock_file):
        lifespan_logger.save_raw()

    mock_file.assert_called_once_with(lifespan_logger.file_path('raw.json'), 'w')
    mock_file().write.assert_called()

def test_save_mathematical_analysis(lifespan_logger):
    mock_file = MagicMock()
    lifespan_logger.enrich_dataframe()
    with patch('builtins.open', mock_file):
        lifespan_logger.save_mathematical_analysis()

    mock_file.assert_called_once_with(lifespan_logger.file_path('math.json'), 'w')
    mock_file().write.assert_called()
