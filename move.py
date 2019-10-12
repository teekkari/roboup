from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveSteering


class Driver:
    def __init__(self):
        self.driver = MoveSteering(OUTPUT_B, OUTPUT_C)
        self.speed = SpeedPercent(30)

    
    def move(self, speed):
        self.driver.on(0, self.speed)

    def stop(self):
        self.driver.off()

    def turn(self, steering):
        self.driver.on(steering, self.speed)