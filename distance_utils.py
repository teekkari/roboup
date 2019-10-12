from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.motor import SpeedPercent


class IRUtils:
    def __init__(self):
        self.ir = InfraredSensor()
        self.ir.mode = 'IR-PROX'
        self.speed = SpeedPercent(30)

    def set_speedpc(self, percentage):
        if percentage >= 0 and percentage <= 100:
            self.speed = SpeedPercent(percentage)

    def get_distance_cm(self):
        MAX_DIST = 70
        print(self.ir.proximity, "%")
        print(self.ir.proximity / 100.0 * MAX_DIST, "cm")
        return self.ir.proximity / 100.0 * MAX_DIST

    def get_distance_per(self):
        return self.ir.proximity


    # assuming ir sensor is looking at the right side
    # returns
    # positive = turn right
    # negative = turn left
    # 0 = bumped
    def hold_distance(self, target_distance):

        ERR_MARGIN = 1 # cm

        bump = False

        while not bump:
            dist = self.get_distance_cm()
            delta = dist - target_distance

            # do nothing if we havent passed error threshold
            if abs(delta) < ERR_MARGIN or delta == 0.0:
                continue
            
            return delta
        
        return 0


    def find_target_distance(self, target_distance):
        ERR_MARGIN = 0.2 #cm

        while abs(self.get_distance_cm() - target_distance) > ERR_MARGIN:
            continue
        
        return self.get_distance_cm() - target_distance

