from human_brain_optimizer.models.actions.base import BaseAction


class Sleep(BaseAction):
    ACTION_NAME = 'sleep'
    DEEP_SLEEP_REWARD = 3
    LIGHT_SLEEP_REWARD = 1

    @classmethod
    def run(cls, human):
        if human.last_action == cls.ACTION_NAME:
            human.energy_level += cls.DEEP_SLEEP_REWARD
        else:
            human.energy_level += cls.LIGHT_SLEEP_REWARD
        human.sanitize()
