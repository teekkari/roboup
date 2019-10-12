from ev3dev2.motor import Motor, OUTPUT_B, OUTPUT_C, OUTPUT_D, MoveTank, SpeedPercent
from ev3dev2.sensor.lego import InfraredSensor

ir = InfraredSensor(OUTPUT_D)
ir.mode = 'IR-REMOTE'

tank = MoveTank(OUTPUT_B, OUTPUT_C)
"""
buttons = [
    (ir.REMOTE.RED_UP, ir.REMOTE.RED_DOWN),
    (ir.REMOTE.BLUE_UP, ir.REMOTE.BLUE_DOWN),
]"""

def top_left_channel_1_action():
    tank.run_forever(speed_sp=100)
    print("forward")

def bot_left_channel_1_action():
    tank.run_forever(speed_sp=100)
    print("backward")

def top_right_channel_1_action():
    tank.on_for_degrees(0, SpeedPercent(30), 90)
    print("right")

def bot_right_channel_1_action():
    tank.on_for_degrees(0, SpeedPercent(30), -90)
    print("left")


def remote():
    try:
        ir.on_channel1_top_left = top_left_channel_1_action()
        ir.on_channel1_bottom_left = bot_left_channel_1_action()
        ir.on_channel1_top_right = top_right_channel_1_action()
        ir.on_channel1_bottom_right = bot_right_channel_1_action()
        while True:
            ir.process()
            time.sleep(0.01)
    except:
        tank.stop()