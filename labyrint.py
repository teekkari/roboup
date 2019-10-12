from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, OUTPUT_C, OUTPUT_B, MoveTank
from ev3dev2.motor import MoveDifferential
from ev3dev2.sensor.lego import ColorSensor
from time import sleep
from move import Driver
from distance_utils import IRUtils

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
        speed = 400

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

        factor_negative = (self.correct_value - self.too_dark) / 100
        factor_positive = (self.too_light - self.correct_value) / 100
        factor = (self.too_light - self.correct_value) / (self.correct_value - self.too_dark)

        # if value is 0 turned to left last
        turn = -1

        turn_speed_value = 200

        while not self.end:
            measured_value = cs.value()
            
            color = 6

            while color == 6:
                error = measured_value - target_value
                integral += (error * dt)
                derivative = (error - previous_error) / dt

                if error < 0:
                    u = (Kp * factor * factor_negative * error) + (Ki * integral) + (Kd * derivative)
                else:
                    u = (Kp * factor_positive * error) + (Ki * integral) + (Kd * derivative)
                


                if speed + abs(u) > 1000:
                    if u >= 0:
                        u = 1000 - speed
                    else:
                        u = speed - 1000

                if u < 0:
                    lm.run_timed(time_sp=dt, speed_sp=speed - abs(u), stop_action=stop_action)
                    rm.run_timed(time_sp=dt, speed_sp=speed + abs(u), stop_action=stop_action)
                    sleep(dt / 2000)
                else:
                    lm.run_timed(time_sp=dt, speed_sp=speed + abs(u), stop_action=stop_action)
                    rm.run_timed(time_sp=dt, speed_sp=speed - abs(u), stop_action=stop_action)
                    sleep(dt / 2000)

                color = cs.color
                previous_error = error


            found_white = False
            count = 25

            while not found_white:
                left_number = 0
                count *= 2.5

                while not found_white:

                    lm.run_timed(time_sp=dt, speed_sp = -1 * turn * turn_speed_value, stop_action=stop_action)
                    rm.run_timed(time_sp=dt, speed_sp = turn * turn_speed_value, stop_action=stop_action)

                    if cs.color == 6:
                        lm.run_timed(time_sp=dt, speed_sp = -1 * turn * turn_speed_value, stop_action=stop_action)
                        rm.run_timed(time_sp=dt, speed_sp = turn * turn_speed_value, stop_action=stop_action)
                        found_white = True
                        turn *= -1

                    if left_number >= count:
                        break
                    
                    left_number += 1
                

                turn *= -1



start_dist = IRUtils().get_distance_cm()

cs = ColorSensor()
driver = Driver()
driver.set_speed(600)



found_color = False
while not found_color:
    
    if cs.color() == 6:
        break

lineFollower = LineFollower(60, 20, 90)
lineFollower.run()