from bot_base import Bot
from drop_dens import stop_dens

import time

class Dens(Bot):
    def __init__(self):

        super().__init__(False)

        self.moveset = [
            "setspeed 20",
            "forward for 30",
            "seekwall",
            "turn 5",
            "sleep 0.5",
            "setspeed 30",
            "forward for 65",
            "turn 150",
            "setspeed 30",
            "reverse 45",
            "forward for 7",
            "turn -95",
            "reverse 20",
            "sleep 0.2",
            "forward for 3",
            "sleep 0.2",
            "turn 3",
            "seekwall",
            "setspeed 20",
            "sleep 0.5",
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
            "turn 40",
            "sleep 0.5",
            "forward for 69",
            "setspeed 40"
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