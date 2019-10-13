from distance_utils import IRUtils
from bot_base import Bot

from drop_dens import read_dens, setup_dens

import time

if __name__=="__main__":
    ir = IRUtils()

    read_dens()

    setup_dens(0)

    read_dens()
    


    #bot.seek_wall_parallel()

    #bot.victory()

    #while True:
    d = ir.get_distance_cm()
    v = ir.get_ir_value()
    print("prox {:.2f} cm, ir.value {:.2f} pc".format(d, v))