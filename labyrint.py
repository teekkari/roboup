from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, OUTPUT_C, OUTPUT_B, MoveTank
from ev3dev2.motor import MoveDifferential
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

lm = LargeMotor(OUTPUT_B)
rm = LargeMotor(OUTPUT_C)

cs = ColorSensor()
cs.mode = 'COL-REFLECT'

drive_obj = MoveTank(OUTPUT_B, OUTPUT_C)    

rm.run_timed(time_sp=4000, speed_sp=750)
lm.run_timed(time_sp=4000, speed_sp=750)



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

        # PID tuning
        Kp = 1  # proportional gain
        Ki = 0  # integral gain
        Kd = 0  # derivative gain

        target_value = self.correct_value

        count = 0
        integral = 0

        previous_error = 0

        while not self.end:
            print(cs.value())
            error = target_value - cs.value()
            integral += (error * dt)
            derivative = (error - previous_error) / dt
            u = (Kp * error) + (Ki * integral) + (Kd * derivative)

            if speed + abs(u) > 1000:
                if u >= 0:
                    u = 1000 - speed
                else:
                    u = speed - 1000

            
            if u >= 0:
                lm.run_timed(time_sp=dt, speed_sp=speed + u, stop_action=stop_action)
                rm.run_timed(time_sp=dt, speed_sp=speed - u, stop_action=stop_action)
                sleep(dt / 1000)
            else:
                lm.run_timed(time_sp=dt, speed_sp=speed - u, stop_action=stop_action)
                rm.run_timed(time_sp=dt, speed_sp=speed + u, stop_action=stop_action)
                sleep(dt / 1000)

            previous_error = error
            count += 1

            if count > 200:
                self.shut_down = True


lineFollower = LineFollower(28, 18, 62)
lineFollower.run()