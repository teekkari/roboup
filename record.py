import pickle
import time
from move import Driver
import sys

class Record():

    def __init__(self):
        self.name = sys.argv[1]
        with open(self.name + '.pkl', 'rb') as f:
            self.ghost = pickle.load(f)
        self.driver = Driver()
        self.driver.set_speed(15)
    

    def play(self):
        print(len(self.ghost))
        for move in self.ghost:
            time.sleep(0.3)
            now = time.time()
            if move[0] == 'forward':
                self.driver.move()
                while True:
                    if time.time() - now > move[1]:
                        self.driver.stop()
                        break
            if move[0] == 'backward':
                self.driver.reverse()
                while True:
                    if time.time() - now > move[1]:
                        self.driver.stop()
                        break
            if move[0] == 'right':
                self.driver.turn(100)
                while True:
                    if time.time() - now > move[1]:
                        self.driver.stop()
                        break
            if move[0] == 'left':
                self.driver.turn(-100)
                while True:
                    if time.time() - now > move[1]:
                        self.driver.stop()
                        break
        print("Recording ending.")

if __name__ == "__main__":
    r = Record()
    r.play()