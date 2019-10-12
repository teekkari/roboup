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
driver.set_speed(40)

driver.move()

safe_threshold = 20

while True:
    
    distance_from_wall = utils.get_distance_cm()
    print(distance_from_wall)

    if distance_from_wall < safe_threshold:
        driver.turn_degrees(20)
        driver.move_seconds(1)

    if cs.color == 6:
        break

lineFollower = LineFollower(60, 20, 90)
lineFollower.run(4)

driver.move_seconds(2)
driver.set_speed(-70)

sleep(10)

driver.move_seconds(2)
driver.turn_degrees(-90)

lineFollower.run(100)
