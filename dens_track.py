from bot_base import Bot

class Dens(Bot):
    def __init__(self):

        super().__init__(False)

        self.moveset = [
            "forward for 25",
            "turn 15",
            "setspeed 35",
            "forward for 30",
            "setspeed 20",
            "turn -20",
            "find 13",
            "setspeed 30",
            "forward for 50",
            "turn 180",
            "reverse 20"
        ]

        self.b = [
            "forward for 3",
            "turn -90",
            "forward 40",
            "dens drop",
            "reverse 5",
            "sleep "
        ]

    def run(self):
        for move in self.moveset:
            self.parse_move(move)


if __name__=="__main__":
    t = Dens()
    t.run()