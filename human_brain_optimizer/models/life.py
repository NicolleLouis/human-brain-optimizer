from human_brain_optimizer.models.human import Human


class Life:
    def __init__(self):
        self.human = Human()

    def run(self):
        while self.human.dead is False:
            self.human.turn_consequence()
