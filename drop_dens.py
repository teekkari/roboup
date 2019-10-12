from ev3dev2.motor import MediumMotor, OUTPUT_D, SpeedPercent
import time

def drop_dens():
    med_motor = MediumMotor(OUTPUT_D)

    med_motor.on_for_degrees(SpeedPercent(95), 90)
    time.sleep(1.0)
    med_motor.on_for_degrees(SpeedPercent(95), -90)

drop_dens()


