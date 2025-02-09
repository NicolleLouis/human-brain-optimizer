from human_brain_optimizer.models.human import Human
from human_brain_optimizer.models.logger.action import ActionLogger


class Life:
    def __init__(self):
        self.human = Human()
        self.action_logger = ActionLogger()

    def run(self):
        while self.human.dead is False:
            action = self.human.turn()
            self.action_logger.log(action)
