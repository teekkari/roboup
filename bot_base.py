from move import Driver
from distance_utils import IRUtils
from ev3dev2.sensor.lego import TouchSensor, ColorSensor

import time

# commands
# forward
#   for
#       int(cm_dist)
#   until
#       color
#           int(color)
#       wall
#       finish
# reverse
#   int(cm_dist)
# find [moves forward until]
#   int(cm_dist_from_wall)
# hold [hugs the wall with dist]
#   int(cm_dist_from_wall)


class Bot:

    def __init__(self):

        self.moveset = [
            "forward for 30",
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
            "turn -90"
            "forward until finish" #forward until finish
        ]

        self.driver = Driver()
        self.irutils = IRUtils()
        self.ts = TouchSensor()
        self.cs = ColorSensor()


    def run(self):
        for move in self.moveset:
            self.parse_move(move)


    def parse_move(self, move):
        args = move.split(" ")

        if args[0] == "find":
            self.driver.move()
            self.irutils.find_target_distance(int(args[1]))
            self.driver.stop()
        elif args[0] == "sleep":
            time.sleep(int(args[1]))
        elif args[0] == "hold":
            target_dist = int(args[1])

            d = self.irutils.get_turn_from_dist(target_dist)
            self.driver.turn(int(d))

            while True:
                self.driver.move()
                d = self.irutils.hold_distance(target_dist)

                if d == 0: # bump
                    break
                elif abs(d) > (target_dist + 5): # gap encountered
                    break

                self.driver.stop()
                self.driver.turn(int(d))
                self.irutils.find_target_distance(target_dist)
                self.driver.stop()
        elif args[0] == "turn":
            self.driver.turn_degrees(int(args[1]))
        elif args[0] == "forward":
            if args[1] == "for":
                self.driver.move_cm(int(args[2]))
            elif args[1] == "until":
                if args[2] == "color":
                    self.driver.move()
                    while self.cs.color != int(args[3]):
                        time.sleep(0.01) #10ms
                    self.driver.stop()
                    pass # color sensor color int(args[3])
                elif args[2] == "wall":
                    self.driver.move()
                    self.ts.wait_for_pressed()
                    self.driver.stop()
                    pass # touch sensor pressed
                elif args[2] == "finish":
                    pass # idk lol


            




    