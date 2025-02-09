import os
import sys
from abc import ABC, abstractmethod
from pathlib import Path

from human_brain_optimizer.exceptions.models.logger import LoggerMissingImplementationException


class BaseLogger(ABC):
    BASE_FILE_NAME = None

    PROJECT_ROOT = Path(sys.path[0])
    LOGS_DIRECTORY = PROJECT_ROOT / "log"

    def __init__(self):
        if self.BASE_FILE_NAME is None:
            raise LoggerMissingImplementationException

    @abstractmethod
    def log(self, message) -> None:
        pass

    def file_name(self):
        self.LOGS_DIRECTORY.mkdir(parents=True, exist_ok=True)
        return str(self.LOGS_DIRECTORY / f"{self.BASE_FILE_NAME}.json")

    @abstractmethod
    def save(self) -> None:
        pass
