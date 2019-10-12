from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.motor import SpeedPercent

import time


class IRUtils:
    def __init__(self):
        self.ir = InfraredSensor()
        self.ir.mode = 'IR-PROX'
        self.speed = SpeedPercent(30)
        self.ts = TouchSensor()

    def set_speedpc(self, percentage):
        if percentage >= 0 and percentage <= 100:
            self.speed = SpeedPercent(percentage)

    def get_distance_cm(self):
        MAX_DIST = 70
        dist = self.ir.proximity / 100.0 * MAX_DIST
        #print(" {:.2f} cm".format(dist))
        return dist / 2


    def get_ir_value(self):
        return self.ir.value()

    def get_distance_per(self):
        return self.ir.proximity


    # assuming ir sensor is looking at the right side
    # returns
    # positive = turn right
    # negative = turn left
    # 0 = bumped
    def hold_distance(self, target_distance, sensorOnRightSide):

        ERR_MARGIN = 5 # cm
        TURN_CONST = 1

        while self.ts.is_pressed == 0:
            dist = self.get_distance_cm()
            delta = dist - target_distance

            # do nothing if we havent passed error threshold
            if abs(delta) < ERR_MARGIN or delta == 0.0:
                # time.sleep(0.005) #5ms
                continue

            print("delta:", delta, "ts:", self.ts.is_pressed)
            

            if sensorOnRightSide:
                return delta*TURN_CONST
            else:
                return -delta*TURN_CONST
        
        return 0


    def get_turn_from_dist(self, target_distance):
        TURN_CONST = 0.5
        dist = self.get_distance_cm()
        delta = dist - target_distance

        return delta*TURN_CONST

    def find_target_distance(self, target_distance):
        ERR_MARGIN = 10 #cm

        while abs(self.get_distance_cm() - target_distance) > ERR_MARGIN:
            continue

        print(self.get_distance_cm() - target_distance, "ftd")
        return self.get_distance_cm() - target_distance

