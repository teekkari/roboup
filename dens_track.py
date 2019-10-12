from bot_base import Bot

class Dens(Bot):
    def __init__(self):

        super().__init__(False)

        self.moveset = [
            "find 20",
            "hold 20",
        ]

        self.moveset2 = [
            "forward for 50",
            "turn -20",
            "find 5",
            "hold 5",
            "reverse 30",
            "turn 90",
            "forward until color 6", #foward until color 6 white
            "dropdens",
            "turn 90",
            "sleep 5"
            "forward until wall", # forward until wall
            "turn -90",
            "forward until finish" #forward until finish
        ]

    def run(self):
        for move in self.moveset:
            self.parse_move(move)


if __name__=="__main__":
    t = Dens()
    t.run()