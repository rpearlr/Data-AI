from multiprocessing import Process,Pool
import time

def worker() :
    print("Worker is running")

def worker_2() :
    q.put("Hello")

    
def square(n) :
  return  n*n

if __name__ == "__main__" : 
    # num = [10**7,10**2,10**3]
    # start = time.time()
    # with Pool() as p:
    #     results = p.map(square,num)
    # end=time.time()

    # print("Results : ",results)
    # print("Time : ", end-start)
    q = Queue()
    p =Process(target=worker_2)
        