from collections import Counter

from human_brain_optimizer.models.human import Human


class InventoryService:
    @staticmethod
    def generate_condensed_format(human: Human):
        return dict(Counter(human.inventory))
