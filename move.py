from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveSteering


class Driver:
    def __init__(self):
        self.driver = MoveSteering(OUTPUT_B, OUTPUT_C)
        self.speed = 40


    def set_speed(self, speed):
        self.speed = max(-100, max(100, speed))

    
    def move(self):
        self.driver.on(0, SpeedPercent(self.speed))

    def reverse(self):
        self.driver.on(0, SpeedPercent(-self.speed))

    def stop(self):
        self.driver.off()

    def turn(self, steering):
        steering = max(-100, min(100, steering))
        self.driver.on(steering, self.speed)

    def turn_rotations(self, steering, rotations):
        steering = max(-100, min(100, steering))
        self.driver.on_for_rotations(steering, SpeedPercent(self.speed), rotations)

    def turn_degrees(self, degrees):
        TRANSFORM_CONST = 0.2
        steering = 100 if degrees > 0 else -100
        self.driver.on_for_rotations(steering, SpeedPercent(self.speed), degrees * TRANSFORM_CONST)