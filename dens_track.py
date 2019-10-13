from bot_base import Bot
from drop_dens import stop_dens

import time

class Dens(Bot):
    def __init__(self):

        super().__init__(False)

        stop_dens()
        print("dens stop")
        time.sleep(2)

        self.moveset = [
            "forward for 30",
            "seekwall",
            "turn 8",
            "sleep 0.5",
            "setspeed 25",
            "forward for 60",
            "setspeed 15",
            "turn 160",
            "setspeed 20",
            "reverse 45",
            "forward for 7",
            "turn -95",
            "reverse 10",
            "forward for 3",
            "turn 5",
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
            "turn 50",
            "sleep 0.5",
            "forward for 65"
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