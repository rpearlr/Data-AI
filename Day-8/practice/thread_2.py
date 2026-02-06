import threading
import time

def greet(name) :
    time.sleep(2)
    print(f"Hello {name}")

t = threading.Thread(target=greet,args=("Alice",))
t.start()

greet("Alice")