import time
import threading
from urllib.request import urlretrieve

def worker(num) : 
    print(f"Worker {num} is working")
    time.sleep(2)
    print(f"Worker {num} is finished")

# for i in range (5) :
    # t=threading.Thread(target=worker,args=(i,))
    # t.start()

destination = 'pdf_stress.pdf'
def download() :
    url  = "https://www.uakron.edu/armyrotc/ms1/14.pdf"
    filename,headers = urlretrieve(url,destination)
    time.sleep(2)
    print(f"File '{filename}' downloaded successfully.")

t = threading.Thread(target=download)
t.start()
# t.join()

