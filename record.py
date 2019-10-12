import pickle
import time
from move import Driver
import argparse

class Record():

    def __init__(self):
        self.name = self.parse_args()
        with open(self.name + '.pkl', 'rb') as f:
            self.ghost = pickle.load(f)
        self.driver = Driver()
    
    def parse_args(self):
        parser = argparse.ArgumentParser(description='Enter filename for recording')
        parser.add_argument('-n', help='Enter filename for the track')
        args = parser.args
        print(args)
        if not args:
            raise Exception("Please enter filename after -n argument")
        return args

    def play(self):
        print(len(self.ghost))
        for move in self.ghost:
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