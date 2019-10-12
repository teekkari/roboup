from distance_utils import IRUtils

if __name__=="__main__":
    ir = IRUtils()

    while True:
        print("{:.2f} cm".format(ir.get_distance_cm))