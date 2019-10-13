from bot_base import Bot

class Dens(Bot):
    def __init__(self):

        super().__init__(False)

        self.moveset = [
            "forward for 25",
            "turn 30",
            "setspeed 35",
            "forward for 25",
            "setspeed 20",
            "turn -25",
            "find 13",
            "sleep 1",
            "setspeed 30",
            "forward for 65",
            "setspeed 20",
            "turn 180",
            "reverse 30",
            "forward for 10",
            "turn -90",
            "seekwall",
            "forward for 35",
            "dens drop",
            "reverse 8",
            "sleep 1",
            "dens lift",
            "sleep 8",
            "turn 20",
            "forward for 15"
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