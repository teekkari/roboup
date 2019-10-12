from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_C, OUTPUT_B, MoveTank
from ev3dev2.motor import MoveDifferential
from ev3dev2.sensor.lego import ColorSensor



from move import Driver

lm = LargeMotor(OUTPUT_B)
rm = LargeMotor(OUTPUT_C)

driver = Driver()

driver.set_speed(70)
driver.move_seconds(3)

driver.reverse()
cs = ColorSensor()

driver.stop()

driver.turn_degrees(-90)

driver.back_seconds(3)

driver.move_seconds(0.2)

driver.turn_degrees(90)

driver.back_seconds(3)
driver.move_seconds(0.2)

driver.turn_degrees(-90)




