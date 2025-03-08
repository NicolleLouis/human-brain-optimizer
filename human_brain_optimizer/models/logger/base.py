import sys
from abc import ABC, abstractmethod
from pathlib import Path

from human_brain_optimizer.exceptions.models.logger import LoggerMissingImplementationException


class BaseLogger(ABC):
    BASE_FILE_DIRECTORY = None

    PROJECT_ROOT = Path(sys.path[0])
    LOGS_DIRECTORY = PROJECT_ROOT / "log"

    def __init__(self):
        if self.BASE_FILE_DIRECTORY is None:
            raise LoggerMissingImplementationException

    @abstractmethod
    def log(self, **kwargs) -> None:
        pass

    def file_path(self, filename = "raw.json"):
        self.LOGS_DIRECTORY.mkdir(parents=True, exist_ok=True)

        subdirectory = self.LOGS_DIRECTORY / self.BASE_FILE_DIRECTORY
        subdirectory.mkdir(parents=True, exist_ok=True)

        return str(subdirectory / filename)

    def save_graph(self, chart_name, fig, save_html=False):
        if save_html:
            fig.write_html(self.file_path(f"{chart_name}.html"))
        fig.write_image(self.file_path(f"{chart_name}.png"))

    @abstractmethod
    def save(self, raw_values=False, extensive=False) -> None:
        pass

    @abstractmethod
    def merge_logger(self, other_logger) -> None:
        pass

    def reset(self) -> None:
        self.__init__()
