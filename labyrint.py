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
        speed = 360/2

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

        turn_speed = 10

        # if value is 0 turned to left last
        last_turn = 1

        while not self.end:
            measured_value = cs.value()
            
            color = 6

            while color == 6:
                error = measured_value - target_value
                print(error)
                print(error > 0)
                integral += (error * dt)
                derivative = (error - previous_error) / dt

                if error < 0:
                    u = (Kp * factor * factor_negative * error) + (Ki * integral) + (Kd * derivative)
                else:
                    u = (Kp * factor_positive * error) + (Ki * integral) + (Kd * derivative)
                


                if speed + pow(abs(u),2) > 1000:
                    if u >= 0:
                        u = 1000 - speed
                    else:
                        u = speed - 1000

                if u < 0:
                    lm.run_timed(time_sp=dt, speed_sp=speed - abs(u), stop_action=stop_action)
                    rm.run_timed(time_sp=dt, speed_sp=speed + abs(u), stop_action=stop_action)
                    last_turn = 0
                    sleep(dt / 2000)
                else:
                    lm.run_timed(time_sp=dt, speed_sp=speed + abs(u), stop_action=stop_action)
                    rm.run_timed(time_sp=dt, speed_sp=speed - abs(u), stop_action=stop_action)
                    last_turn = 1
                    sleep(dt / 2000)

                color = cs.color
                previous_error = error


            found_white = False
            count = 4
            while not found_white:
                left = False
                left_number = 0
                count *= 2.5

                while not left and not found_white:

                    lm.run_timed(time_sp=dt, speed_sp=-70, stop_action=stop_action)
                    rm.run_timed(time_sp=dt, speed_sp=70, stop_action=stop_action)

                    if cs.color == 6:
                        found_white = True

                    if left_number >= count:
                        break
                    
                    
                right = False
                right_number = 0
                count *= 2.5

                while not right and not found_white:

                    lm.run_timed(time_sp=dt, speed_sp=70, stop_action=stop_action)
                    rm.run_timed(time_sp=dt, speed_sp=-70, stop_action=stop_action)

                    if cs.color == 6:
                        found_white = True

                    if right_number >= count:
                        break

            


lineFollower = LineFollower(60, 20, 90)
lineFollower.run()