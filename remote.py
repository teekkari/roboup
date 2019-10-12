from ev3dev2.sensor.lego import InfraredSensor
from move import Driver
import sys
import time
import pickle

class Remote():
    def __init__(self):
        self.ir = InfraredSensor()
        self.ir.mode = 'IR-REMOTE'
        self.drive = Driver()
        self.ir.on_channel1_beacon = self.beacon_channel_1_action
        self.ir.on_channel1_top_left = self.top_left_channel_1_action
        self.ir.on_channel1_bottom_left = self.bot_left_channel_1_action
        self.ir.on_channel1_top_right = self.top_right_channel_1_action
        self.ir.on_channel1_bottom_right = self.bot_right_channel_1_action
        self.name = sys.argv[1]
        self.ghost = []
        self.now = 0

    def beacon_channel_1_action(self, state):
        print(self.ir.beacon())
        if state:
            print("Beacon pressed, now stopping")
            with open(self.name + '.pkl', 'wb') as f:
                pickle.dump(self.ghost, f)

    def top_left_channel_1_action(self, state):
        print(self.ir.top_left())
        if state:
            self.now = time.time()
            self.drive.move()
        else:
            self.ghost.append(('forward', time.time() - self.now))
            self.drive.stop()

    def bot_left_channel_1_action(self, state):
        print(self.ir.bottom_left())
        if state:
            self.now = time.time()
            self.drive.reverse()
        else:
            self.ghost.append(('backward', time.time() - self.now))
            self.drive.stop()

    def top_right_channel_1_action(self, state):
        print(self.ir.top_right())
        if state:
            self.now = time.time()
            self.drive.turn(100)
        else:
            self.ghost.append(('right', time.time() - self.now))
            self.drive.stop()

    def bot_right_channel_1_action(self, state):
        print(self.ir.bottom_right())
        if state:
            self.now = time.time()
            self.drive.turn(-100)
        else:
            self.ghost.append(('left', time.time() - self.now))
            self.drive.stop()

    def remote(self):
        try:
            while True:
                self.ir.process()
                time.sleep(0.01)
        except Exception as e:
            print(e)
            self.drive.stop()

if __name__ == "__main__":
    r = Remote()
    r.remote()