from ev3dev2.motor import Motor, OUTPUT_B, OUTPUT_C, MoveTank, SpeedPercent
from ev3dev2.sensor.lego import InfraredSensor
from move import Driver


class Remote():
    def __init__(self):
        self.ir = InfraredSensor()
        self.ir.mode = 'IR-REMOTE'
        self.drive = Driver()
        self.ir.on_channel1_beacon = beacon_channel_1_action
        self.ir.on_channel1_top_left = top_left_channel_1_action
        self.ir.on_channel1_bottom_left = bot_left_channel_1_action
        self.ir.on_channel1_top_right = top_right_channel_1_action
        self.ir.on_channel1_bottom_right = bot_right_channel_1_action

    def beacon_channel_1_action(self, state):
        if state:
            print("Beacon pressed, now stopping")
            self.drive.stop()

    def top_left_channel_1_action(self, state):
        if state:
            self.drive.move()
            print("forward")
        else:
            self.drive.stop()

    def bot_left_channel_1_action(self, state):
        if state:
            self.drive.reverse()
            print("backward")
        else:
            self.drive.stop()

    def top_right_channel_1_action(self, state):
        if state:
            self.drive.turn(50)
            print("right")
        else:
            self.drive.stop()

    def bot_right_channel_1_action(self, state):
        if state:
            self.drive.turn(-50)
            print("left")
        else:
            self.drive.stop()

    def remote():
        try:
            while True:
                ir.process()
                time.sleep(0.01)
        except:
            self.drive.stop()

if __name__ == "__main__":
    r = Remote()
    r.remote()