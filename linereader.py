from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, OUTPUT_B, OUTPUT_C, MoveSteering
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.button import Button

from time import sleep

class LineFollower:
    # Constructor
    def __init__(self):
        self.shut_down = False

    # Main method
    def run(self):

        # sensors
        cs = ColorSensor() 

        cs.mode = 'COL-REFLECT'  # measure light intensity

        # motors
        lm = LargeMotor('outB')
        rm = LargeMotor('outC')

        speed = 360/2  # deg/sec, [-1000, 1000]
        dt = 500       # milliseconds
        stop_action = "coast"

        # PID tuning
        Kp = 1  # proportional gain
        Ki = 0.005  # integral gain
        Kd = 0.01  # derivative gain

        integral = 0
        previous_error = 0

        # initial measurment
        target_value = 30

        # Start the main loop
        while not self.shut_down:

            # Calculate steering using PID algorithm
            error = target_value - cs.value()
            integral += (error * dt)
            derivative = (error - previous_error) / dt

            # u zero:     on target,  drive forward
            # u positive: too bright, turn right
            # u negative: too dark,   turn left

            u = (Kp * error) + (Ki * integral) + (Kd * derivative)

            # limit u to safe values: [-1000, 1000] deg/sec
            if speed + abs(u) > 1000:
                if u >= 0:
                    u = 1000 - speed
                else:
                    u = speed - 1000

            # run motors
            if u < 0:
                lm.run_timed(time_sp=dt, speed_sp=speed + abs(u), stop_action=stop_action)
                rm.run_timed(time_sp=dt, speed_sp=speed - abs(u), stop_action=stop_action)
                sleep(dt / 1000)
            else:
                lm.run_timed(time_sp=dt, speed_sp=speed - abs(u), stop_action=stop_action)
                rm.run_timed(time_sp=dt, speed_sp=speed + abs(u), stop_action=stop_action)
                sleep(dt / 1000)

            previous_error = error

line = LineFollower()
line.run()
