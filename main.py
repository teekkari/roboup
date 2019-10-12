#!/usr/bin/env python3

# main file of the bot


from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from drop_dens import drop_dens
from ir_remote import remote
from linereader import LineFollower


def run_bot():

    LineFollower.run()

    drive_obj = MoveTank(OUTPUT_B, OUTPUT_C)
    cs = ColorSensor()
    drop_dens()
    remote()
    cs.mode = 'COL-COLOR'
    end = True
    while end:
        drive_obj.on_for_degrees(0, SpeedPercent(30), 90)
        if cs.color == 6:
            end = False

if __name__ == "__main__":
    run_bot()