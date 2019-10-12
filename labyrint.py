from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, OUTPUT_C, OUTPUT_B, MoveTank
from ev3dev2.motor import MoveDifferential
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

lm = LargeMotor(OUTPUT_B)
rm = LargeMotor(OUTPUT_C)

drive_obj = MoveTank(OUTPUT_B, OUTPUT_C)    

class LineFollower():
    def __init__(self, correct_value, too_dark, too_light):
        self.correct_value = correct_value
        self.too_dark = too_dark
        self.too_light = too_light
        self.end = False

    def run(self):
        dt = 500
        stop_action = "coast"
        speed = 360/4

        cs = ColorSensor()
        cs.mode = 'COL-REFLECT'

        # PID tuning
        Kp = 1  # proportional gain
        Ki = 0  # integral gain
        Kd = 0  # derivative gain

        target_value = self.correct_value

        count = 0
        integral = 0

        previous_error = 0

        # if value is 0 turned to left last
        last_turn = 1

        while not self.end:
            measured_value = cs.value()

            error = measured_value - target_value
            print(error)
            integral += (error * dt)
            derivative = (error - previous_error) / dt
            u = (Kp * error) + (Ki * integral) + (Kd * derivative)

            if speed + abs(u) > 1000:
                if u >= 0:
                    u = 1000 - speed
                else:
                    u = speed - 1000

            if u < 0:
                lm.run_timed(time_sp=dt, speed_sp=speed - abs(u), stop_action=stop_action)
                rm.run_timed(time_sp=dt, speed_sp=speed + u, stop_action=stop_action)
                last_turn = 0
                sleep(dt / 2000)
            else:
                lm.run_timed(time_sp=dt, speed_sp=speed + u, stop_action=stop_action)
                rm.run_timed(time_sp=dt, speed_sp=speed - abs(u), stop_action=stop_action)
                last_turn = 1
                sleep(dt / 2000)
            
             
            
            previous_error = error
            count += 1

            if count > 200:
                self.shut_down = True


lineFollower = LineFollower(28, 18, 62)
lineFollower.run()