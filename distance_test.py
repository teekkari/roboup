from distance_utils import IRUtils

if __name__=="__main__":
    ir = IRUtils()

    while True:
        d = ir.get_distance_cm()
        v = ir.get_ir_value()
        print("prox {:.2f} cm, ir.value {:.2f} pc".format(d, v))