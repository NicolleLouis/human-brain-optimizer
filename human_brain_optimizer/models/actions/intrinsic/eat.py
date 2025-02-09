from human_brain_optimizer.models.actions.base import BaseAction


class Eat(BaseAction):
    ACTION_NAME = 'eat'

    @classmethod
    def run(cls, human):
        if 'rabbit' in human.inventory:
            human.remove_item('rabbit')
            human.food_level += 12
            human.sanitize()
