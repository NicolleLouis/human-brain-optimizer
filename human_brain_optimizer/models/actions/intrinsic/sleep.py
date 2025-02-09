from human_brain_optimizer.models.actions.base import BaseAction


class Sleep(BaseAction):
    ACTION_NAME = 'sleep'

    @classmethod
    def run(cls, human):
        if human.last_action == cls.ACTION_NAME:
            human.energy_level += 3
        else:
            human.energy_level += 1
        human.sanitize()
