from move import Driver

class Track1:

    def __init__(self, bot_obj):
        self.moveset = [
            "find 5",
            "hold 5"
        ]

        self.driver = Driver()


    def run(self):
        for move in self.moveset:
            self.parse_move(move)


    def parse_move(self, move):
        args = move.split(" ")

        if args[0] == "find":
            self.driver.move(20)
            




    