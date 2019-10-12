from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor.lego import TouchSensor


class IRUtils:
    def __init__(self):
        self.ir = InfraredSensor()
        self.ir.mode = 'IR-PROX'

    def get_distance_cm(self):
        MAX_DIST = 70
        print(self.ir.proximity)
        print(self.ir.proximity * MAX_DIST, "cm")
        return self.ir.proximity * MAX_DIST

    def get_distance_per(self):
        return self.ir.proximity


    # assuming ir sensor is looking at the right side
    def hold_distance(self, target_distance, tank, callback):
        ERR_MARGIN = 0.1

        bump = False

        while not bump:
            dist = self.get_distance_cm()
            delta = dist - target_distance

            # do nothing if we havent passed error threshold
            if abs(delta) < ERR_MARGIN:
                continue

            if delta < 0:
                #turn right slightly
                pass
            else:
                #turn left slightly
                pass


