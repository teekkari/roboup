from ev3dev2.sensor.lego import InfraredSensor
from move import Driver
import time

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

    def beacon_channel_1_action(self, state):
        print(self.ir.beacon())
        if state:
            print("Beacon pressed, now stopping")
            self.drive.stop()

    def top_left_channel_1_action(self, state):
        print(self.ir.top_left())
        while state:
            self.drive.move_cm(5)

    def bot_left_channel_1_action(self, state):
        print(self.ir.bottom_left())
        while state:
            self.drive.move_neg_cm(5)

    def top_right_channel_1_action(self, state):
        print(self.ir.top_right())
        while state:
            self.drive.turn_degrees(10)

    def bot_right_channel_1_action(self, state):
        print(self.ir.bottom_right())
        while state:
            self.drive.turn_neg_degrees(10)

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