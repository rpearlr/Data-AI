from multiprocessing import Pool
import time

def simulate(reigon) :
    print(" Calculate for ",reigon)
    time.sleep(2)
    return reigon

if __name__ == "__main__" :
    reigons = {"N","S","E","W"}
    with Pool(processes=4) as p:
        res = p.map(simulate,reigons)
    print(res)