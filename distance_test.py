from distance_utils import IRUtils
from bot_base import Bot

import time

if __name__=="__main__":
    ir = IRUtils()

    bot = Bot(False)

    bot.driver.move()

    time.sleep(2)

    bot.driver.move()

    time.sleep(3)

    bot.driver.stop()


    #bot.seek_wall_parallel()

    #bot.victory()

    #while True:
    d = ir.get_distance_cm()
    v = ir.get_ir_value()
    print("prox {:.2f} cm, ir.value {:.2f} pc".format(d, v))