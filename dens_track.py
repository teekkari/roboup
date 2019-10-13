from bot_base import Bot

class Dens(Bot):
    def __init__(self):

        super().__init__(False)

        self.moveset = [
            "forward for 25",
            "turn 30",
            "setspeed 30",
            "forward for 20",
            "setspeed 20",
            "turn -25",
            "find 10",
            "sleep 1",
            "setspeed 30",
            "forward for 50",
            "setspeed 20",
            "turn 165",
            "reverse 40",
            "forward for 10",
            "turn -95",
            "seekwall",
            "forward for 30",
            "turn -5",
            "sleep 0.2",
            "dens drop",
            "reverse 8",
            "sleep 1",
            "dens lift",
            "reverse 15",
            "sleep 1",
            "turn 40",
            "sleep 0.5",
            "forward for 45"
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