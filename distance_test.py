from distance_utils import IRUtils

if __name__=="__main__":
    ir = IRUtils()

    while True:
        d = ir.get_distance_cm()
        print("prox {:.2f} cm, target delta {:.2f} cm".format(d, 20 - d))