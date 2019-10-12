from ev3dev2.sensor.lego import InfraredSensor


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