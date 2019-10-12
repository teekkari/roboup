from ev3dev2.motor import MediumMotor, OUTPUT_D, SpeedPercent

def drop_dens():
    med_motor = MediumMotor(OUTPUT_D)

    med_motor.on_for_degrees(SpeedPercent(70), 90)

drop_dens()


