import threading
import time
 
def f(i):
    time.sleep(i)
    return
 
# threads
t1 = threading.Thread(target=f, args=(1.2,), name="Thread#1")
t1.start()
 
t2 = threading.Thread(target=f, args=(2.2,), name="Thread#2")
t2.start()
 
for p in range(5):
    time.sleep(p*0.5)
    print('[',time.ctime(),']', t1.getName(), t1.is_alive())
    print('[',time.ctime(),']', t2.getName(), t2.is_alive())