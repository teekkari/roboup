


from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, OUTPUT_C, OUTPUT_B, MoveTank
from ev3dev2.motor import MoveDifferential
from ev3dev2.sensor.lego import ColorSensor
from time import sleep
from move import Driver
from distance_utils import IRUtils
from move import Driver

class LineFollower():
    def __init__(self, correct_value, too_dark, too_light):
        self.correct_value = correct_value
        self.too_dark = too_dark
        self.too_light = too_light
        self.end = False
        self.lm = LargeMotor(OUTPUT_B)
        self.rm = LargeMotor(OUTPUT_C)


    def find_color(self, search = False, safe_from_wall=20):
        utils = IRUtils()

        cs = ColorSensor()
        cs.mode('COL_COLOR')
        driver = Driver()
        driver.set_speed(40)

        driver.move()

        while True:
            distance_from_wall = utils.get_distance_cm()
            print(distance_from_wall)

            if distance_from_wall < safe_from_wall:
                driver.turn_degrees(15)
                driver.move_seconds(0.5)
                driver.move()

            if cs.color == 6:
                break
    

    def run(self, target_color):
        lm = self.lm
        rm = self.rm

        dt = 500
        stop_action = "coast"
        speed = 400

        cs = ColorSensor()
        cs.mode = 'COL-REFLECT'

        # PID tuning
        Kp = 1  # proportional gain
        Ki = 0.01  # integral gain
        Kd = 0.01  # derivative gain

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
            count = 22

            while not found_white:
                left_number = 0
                count *= 2.5

                while not found_white:

                    lm.run_timed(time_sp=dt, speed_sp = -1 * turn * turn_speed_value, stop_action=stop_action)
                    rm.run_timed(time_sp=dt, speed_sp = turn * turn_speed_value, stop_action=stop_action)
                    
                    print(cs.color)
                    if cs.color == 6:
                        lm.run_timed(time_sp=dt, speed_sp = -1 * turn * turn_speed_value, stop_action=stop_action)
                        rm.run_timed(time_sp=dt, speed_sp = turn * turn_speed_value, stop_action=stop_action)
                        found_white = True
                        turn *= -1

                    if left_number >= count:
                        break
                    
                    left_number += 1

                if count > 200:

                    if cs.color == 4:
                        lm.run_timed(time_sp = dt, speed_sp = turn_speed_value, stop_action=stop_action)
                        rm.run_timed(time_sp = dt, speed_sp = turn_speed_value, stop_action=stop_action)
                        Driver().turn_degrees(180)
                        lm.run_timed(time_sp = dt, speed_sp = turn_speed_value, stop_action=stop_action)
                        rm.run_timed(time_sp = dt, speed_sp = turn_speed_value, stop_action=stop_action)

                turn *= -1
