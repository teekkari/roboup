from move import Driver
from ev3dev2.sensor.lego import ColorSensor
import time


class Spin():

    def __init__(self):
        self.drive = Driver()
        self.sensor = ColorSensor()
        
    
    def go(self):
        self.sensor.mode = 'COL-COLOR'
        try:

            self.drive.set_speed(90)
            print("set speed, 90")
            time = time.time()

            
            while time.time() - time < 10:
                self.drive.turn(-20)
            print("Turned left for 10s")
            self.drive.set_speed(50)
            print("Set speed, 50")
            while sensor.color != 6:
                self.drive.turn(10)
                time.sleep(2)
                self.drive.stop()
                self.drive.turn(-20)
                time.sleep(1)
                self.drive.stop()
        except Exception as e:
            print(e)
            self.drive.stop()

if __name__ == "__main__":
    s = Spin()
    s.go()