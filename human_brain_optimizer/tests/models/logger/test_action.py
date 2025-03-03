from unittest.mock import patch, mock_open

import pytest
import pandas as pd

from human_brain_optimizer.models.logger.action import ActionLogger


@pytest.fixture
def empty_logger():
    return ActionLogger()


@pytest.fixture
def logger():
    logger = ActionLogger()
    logger.log('action_1', 10)
    logger.log('action_2', 10)
    logger.log('action_2', 20)
    return logger


def test_log(empty_logger):
    empty_logger.log('action_1', 10)
    empty_logger.log('action_2', 10)
    empty_logger.log('action_2', 20)
    assert empty_logger.action_dict['action_1'] == [10]
    assert empty_logger.action_dict['action_2'] == [10, 20]


def test_merge_logger(empty_logger):
    other_logger = ActionLogger()
    empty_logger.log('action_1', 10)
    other_logger.log('action_1', 20)
    other_logger.log('action_2', 10)
    empty_logger.merge_logger(other_logger)
    assert empty_logger.action_dict['action_1'] == [10, 20]
    assert empty_logger.action_dict['action_2'] == [10]


def test_compute_total_actions(logger):
    logger.compute_total_actions()
    assert logger.total_actions == 3


def test_compute_summarized_values(logger):
    logger.compute_summarized_values()
    assert logger.summarized_actions['action_1'] == 1
    assert logger.summarized_actions['action_2'] == 2


def _test_save_chart(logger, method_name, expected_filename):
    logger.compute_total_actions()
    logger.generate_dataframe()
    logger.compute_summarized_values()
    with patch.object(logger, 'save_graph') as mock_save_graph:
        getattr(logger, method_name)()
        mock_save_graph.assert_called_once()
        args, kwargs = mock_save_graph.call_args
        assert args[0] == expected_filename
        assert args[1] is not None


def test_save_donut_chart(logger):
    _test_save_chart(logger, 'save_donut_chart', 'action_repartition')


def test_save_score_repartition_graph(logger):
    _test_save_chart(logger, 'save_score_repartition_graph', 'score_repartition')


def test_save_normalized(logger):
    logger.compute_summarized_values()
    logger.compute_total_actions()
    with patch('builtins.open', mock_open()) as mocked_file:
        with patch('json.dump') as mock_json_dump:
            logger.save_normalized()
            mocked_file.assert_called_once_with(logger.file_path('normalized.json'), 'w')
            mock_json_dump.assert_called_once()
            args, kwargs = mock_json_dump.call_args
            expected_dict = {'action_1': 33.33, 'action_2': 66.67}
            assert args[0] == expected_dict


def test_generate_dataframe(logger):
    logger.generate_dataframe()
    expected_data = [
        {'action': 'action_1', 'score': 10},
        {'action': 'action_2', 'score': 10},
        {'action': 'action_2', 'score': 20},
        {'action': 'total', 'score': 10},
        {'action': 'total', 'score': 10},
        {'action': 'total', 'score': 20}
    ]

    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(
        logger.df.sort_values(by=['action', 'score']).reset_index(drop=True),
        expected_df.sort_values(by=['action', 'score']).reset_index(drop=True)
    )


def test_save(logger):
    with patch.object(logger, 'save_normalized') as mock_save_normalized, \
            patch.object(logger, 'save_donut_chart') as mock_save_donut_chart, \
            patch.object(logger, 'save_score_repartition_graph') as mock_save_score_repartition_graph:
        logger.save()

        mock_save_normalized.assert_called_once()
        mock_save_donut_chart.assert_called_once()
        mock_save_score_repartition_graph.assert_called_once()
