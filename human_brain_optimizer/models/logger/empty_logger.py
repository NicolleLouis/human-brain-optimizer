from human_brain_optimizer.models.logger.base import BaseLogger


class EmptyLogger(BaseLogger):
    def reset(self) -> None:
        pass

    def log(self, **kwargs) -> None:
        pass

    def save(self) -> None:
        pass

    def merge_logger(self, other_logger) -> None:
        pass

