from move import Driver
from distance_utils import IRUtils

class Track1:

    def __init__(self):
        self.moveset = [
            "find 5",
            "hold 5"
        ]

        self.driver = Driver()
        self.irutils = IRUtils()


    def run(self):
        for move in self.moveset:
            self.parse_move(move)


    def parse_move(self, move):
        args = move.split(" ")

        if args[0] == "find":
            self.driver.move()
            self.irutils.find_target_distance(int(args[1]))
            self.driver.stop()
        elif args[0] == "hold":
            target_dist = int(args[1])
            while True:
                self.driver.move()
                d = self.irutils.hold_distance(target_dist)

                if d == 0: # bump
                    break
                elif abs(d) > (target_dist + 5): # gap encountered
                    break

                self.driver.stop()
                self.driver.turn(int(d * 5))
                self.irutils.find_target_distance(target_dist)
                self.driver.stop()


if __name__=="__main__":
    t = Track1()
    t.run()

            




    