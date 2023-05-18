import threading
import time
 
def f(i):
    for p in range(3):
        time.sleep(i+1.5)
        print(threading.current_thread().getName())
    return
 
# start threads by passing function to Thread constructor
for i in range(3):
    t = threading.Thread(target=f, args=(i,))
    t.setName( 'Thread#'+str(i) )
    t.start()