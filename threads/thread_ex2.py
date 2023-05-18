import threading


def soma(i):
    soma = 0
    for i in range(20*i):
        soma += 1
    print(threading.current_thread().getName(), 'soma ', soma)

lista_threads = list()

for t in range(5):
    th = threading.Thread(target=soma,args=(t+1000000,),name='Threading'+str(t))
    lista_threads.append(th)
    th.start()

print("MEIO")

#for thread in lista_threads:
#    thread.join()
    
print("FINAL")