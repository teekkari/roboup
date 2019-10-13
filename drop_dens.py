from ev3dev2.motor import MediumMotor, OUTPUT_D, SpeedPercent
import time

med_motor = MediumMotor(OUTPUT_D)

def drop_dens():
    med_motor.on_for_degrees(SpeedPercent(95), 90)
    time.sleep(1.0)
    med_motor.on_for_degrees(SpeedPercent(95), -90)


def setup_dens(val):
    med_motor.position = val

def read_dens():
    print(med_motor.position)

def free_dens():
    med_motor.stop_action = 'brake'
    med_motor.command = 'stop'

def stop_dens():
    med_motor.stop_action = 'hold'
    med_motor.command = 'stop'


