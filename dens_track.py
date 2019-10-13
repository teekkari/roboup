from bot_base import Bot

class Dens(Bot):
    def __init__(self):

        super().__init__(False)

        self.moveset = [
            "forward for 30",
            "seekwall",
            "turn 5",
            "sleep 0.5",
            "setspeed 25",
            "forward for 60",
            "setspeed 15",
            "turn 180",
            "setspeed 20",
            "reverse 40",
            "forward for 7",
            "turn -95",
            "reverse 5",
            "seekwall",
            "forward until gap",
            "forward for 20",
            "sleep 0.2",
            "turn -5",
            "sleep 0.2",
            "dens drop",
            "reverse 8",
            "sleep 1",
            "dens lift",
            "reverse 15",
            "sleep 1",
            "turn 45",
            "sleep 0.5",
            "forward for 55"
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