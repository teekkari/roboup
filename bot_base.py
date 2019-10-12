from move import Driver
from distance_utils import IRUtils
from ev3dev2.sensor.lego import ColorSensor, TouchSensor

import time
import math

#### commands
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
# stop [tops all movement]
# find [moves forward until]
#   int(cm_dist_from_wall)
# hold [hugs the wall with dist]
#   int(cm_dist_from_wall)
# seekwall


class Bot:

    def __init__(self, IRSensorsOnRightSide):
        self.driver = Driver()
        self.irutils = IRUtils()
        self.ts = TouchSensor()
        self.cs = ColorSensor()

        self.IRSensorsOnRightSide = IRSensorsOnRightSide


    def parse_move(self, move):
        args = move.split(" ")

        if args[0] == "find":
            self.driver.move()
            self.irutils.find_target_distance(int(args[1]))
            self.driver.stop()
            self.seek_wall_parallel()
        elif args[0] == "seekwall":
            self.seek_wall_parallel()
        elif args[0] == "sleep":
            time.sleep(int(args[1]))
        elif args[0] == "stop":
            self.driver.stop()
        elif args[0] == "hold":
            target_dist = int(args[1])
            while self.ts.is_pressed == 0:
                d = self.irutils.distance_delta(target_dist)

                if abs(d) > 3:
                    if self.IRSensorsOnRightSide:
                        self.driver.turn_degrees(int(d))
                    else:
                        self.driver.turn_degrees(-int(d))

                print("move")
                self.driver.move()
                time.sleep(0.5)

            self.driver.stop()

        elif args[0] == "turn":
            self.driver.turn_degrees(int(args[1]))
        elif args[0] == "reverse":
            self.driver.reverse_cm(int(args[1]))
        elif args[0] == "forward":
            if args[1] == "for":
                self.driver.move_cm(int(args[2]))
            elif args[1] == "until":
                if args[2] == "color":
                    self.driver.move()
                    while self.cs.color != int(args[3]):
                        #time.sleep(0.01) #10ms
                        pass
                    self.driver.stop()
                    pass # color sensor color int(args[3])
                elif args[2] == "wall":
                    self.driver.move()
                    #self.ts.wait_for_pressed()
                    self.driver.stop()
                    pass # touch sensor pressed
                elif args[2] == "finish":
                    pass # idk lol


    def seek_wall_parallel(self):
        TURN_AMT = 6

        old_speed = self.driver.get_speed()
        self.driver.set_speed(10)
        
        dist = self.irutils.get_distance_cm()

        self.driver.turn_degrees(TURN_AMT)
        time.sleep(0.1)

        new_dist = self.irutils.get_distance_cm()

        if new_dist < dist:
            while new_dist < dist:
                self.driver.turn_degrees(TURN_AMT)
                time.sleep(0.1)
                dist = new_dist
                new_dist = self.irutils.get_distance_cm()

            time.sleep(0.1)
            self.driver.turn_degrees(-TURN_AMT / 2)
        else:
            new_dist, dist = dist, new_dist #swap vars
            while new_dist < dist:
                self.driver.turn_degrees(-TURN_AMT)
                time.sleep(0.1)
                dist = new_dist
                new_dist = self.irutils.get_distance_cm()
            
            time.sleep(0.1)
            self.driver.turn_degrees(TURN_AMT / 2)

        self.driver.set_speed(old_speed)


    def victory(self):
        self.driver.turn_degrees(-90)








            




    