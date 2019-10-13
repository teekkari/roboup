from bot_base import Bot

class Dens(Bot):
    def __init__(self):

        super().__init__(False)

        self.moveset = [
            "forward for 20",
            "turn -90",
            "dens drop",
            "reverse 8",
            "sleep 1",
            "dens lift"
        ]

        self.moveset2 = [
            "forward for 20",
            "turn -20",
            "find 10",
            "forward for 60",
            "turn 180",
            "backward 15"
        ]

    def run(self):
        for move in self.moveset:
            self.parse_move(move)


if __name__=="__main__":
    t = Dens()
    t.run()