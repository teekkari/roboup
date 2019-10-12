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

safe_threshold = 20

while True:
    
    distance_from_wall = utils.get_distance_cm()
    print(distance_from_wall)

    if distance_from_wall < safe_threshold:
        driver.turn_degrees(15)
        driver.move_seconds(0.5)
        driver.move()

    if cs.color == 6:
        break

lineFollower = LineFollower(60, 20, 90)
lineFollower.run(4)


distance_from_wall = utils.get_distance_cm()
sleep(5)

driver.reverse()

while distance_from_wall - 4 < utils.get_distance_cm() and distance_from_wall + 4 >= utils.get_distance_cm:
    driver.stop()

driver.turn_degrees(-90)

lineFollower.run(100)
