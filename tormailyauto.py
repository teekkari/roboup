from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_C, OUTPUT_B, MoveTank
from ev3dev2.motor import MoveDifferential
from ev3dev2.sensor.lego import ColorSensor



from move import Driver

lm = LargeMotor(OUTPUT_B)
rm = LargeMotor(OUTPUT_C)

driver = Driver()

driver.set_speed(70)
driver.back_seconds(12)





