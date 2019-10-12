from ev3.ev3dev import Motor, OUTPUT_B, OUTPUT_C, MoveTank
from ev3.lego import InfraredSensor

ir = InfraredSensor()
#ir.mode = 'IR-REMOTE'

tank = MoveTank(OUTPUT_B, OUTPUT_C)
"""
buttons = [
    (ir.REMOTE.RED_UP, ir.REMOTE.RED_DOWN),
    (ir.REMOTE.BLUE_UP, ir.REMOTE.BLUE_DOWN),
]"""

def top_left_channel_1_action(state):
    tank.run_forever(50)

def bot_left_channel_1_action(state):
    tank.run_forever(50)

def top_right_channel_1_action(state):
    tank.on_for_degrees(0, SpeedPercent(30), 90)

def bot_right_channel_1_action(state):
    tank.on_for_degrees(0, SpeedPercent(30), -90)

ir.on_channel1_top_left = top_left_channel_1_action
ir.on_channel1.bottom_left = bot_left_channel_1_action
ir.on_channel1.top_right = top_right_channel_1_action
ir.on_channel1_bottom_right = bot_right_channel_1_action
def remote():
    while True:
        ir.process()
        time.sleep(0.01)