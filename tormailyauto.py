from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_C, OUTPUT_B, MoveTank
from ev3dev2.motor import MoveDifferential
from ev3dev2.sensor.lego import ColorSensor

from distance_utils import IRUtils

utils = IRUtils()

from move import Driver

lm = LargeMotor(OUTPUT_B)
rm = LargeMotor(OUTPUT_C)

driver = Driver()

driver.set_speed(70)
driver.back_seconds(12)

driver.turn_degrees(90)

driver.move()

prev_val = 0.0
while True:
    prev_val = utils.get_distance_cm()

    if prev_val - utils.get_distance_cm() < -10:
        driver.stop()
        break

driver.turn_degrees(90)
driver.back_seconds(5)

driver.move_seconds(0.3)
driver.turn_degrees(90)

driver.back_seconds(3)
driver.move_seconds(0.3)

driver.turn_degrees(-90)

driver.reverse()

dist = utils.get_distance_cm()

while True:

    if dist - utils.get_distance_cm() < -10:
        driver.stop()
        break

driver.turn_degrees(90)
driver.back_seconds(10)