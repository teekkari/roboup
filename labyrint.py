from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, OUTPUT_C, OUTPUT_B, MoveTank
from ev3dev2.motor import MoveDifferential
from ev3dev2.sensor.lego import ColorSensor
from time import sleep
from move import Driver
from distance_utils import IRUtils
from labyrint_main import LineFollower

utils = IRUtils()
start_dist = utils.get_distance_cm()

cs = ColorSensor()
driver = Driver()
driver.set_speed(30)

driver.move()

safe_threshold = 15
max_distance = 16

lm = LargeMotor(OUTPUT_B)
rm = LargeMotor(OUTPUT_C)

while True:
    
    distance_from_wall = utils.get_distance_cm()
    print(distance_from_wall)

    if distance_from_wall < safe_threshold:
        lm = LargeMotor(OUTPUT_B)
        rm = LargeMotor(OUTPUT_C)

        lm.on(30)
        rm.on(20)
        
    if distance_from_wall > max_distance:

        lm.on(20)
        rm.on(30)

    if cs.color == 6:
        break

lineFollower = LineFollower(60, 20, 90)
