#!/usr/bin/env python3

# main file of the bot


from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from drop_tire import drop_dens
from ir_remote import ir_changed


def run_bot():


    drive_obj = MoveTank(OUTPUT_B, OUTPUT_C)
    cs = ColorSensor()
    drop_dens()
    ir_changed()
    end = True
    while end:
        drive_obj.on_for_degrees(SpeedPercent(75), SpeedPercent(75), 1)
        if cs.color() == 6:
            end = False

if __name__ == "__main__":
    run_bot()