from bot_base import Bot

class Dens(Bot):
    def __init__(self):

        super().__init__(False)

        self.moveset = [
            "forward 20",
            "turn -20",
            "find 10",
            "forward 60",
            "turn 180",
            "backward 15"
        ]

    def run(self):
        for move in self.moveset:
            self.parse_move(move)


if __name__=="__main__":
    t = Dens()
    t.run()