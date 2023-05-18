import threading
import numpy as np
from pprint import pprint

thread_size = 4
#mat1 = [[1, 1, 1, 1], [1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1]]
mat1 = np.random.randint(0,5,(1000,1000))
mat1lin = len(mat1)                
mat1col = len(mat1[0])             

#mat2 = [[1, 1, 1, 1], [1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1]]
mat2 = np.random.randint(0,5,(1000,1000))
mat2lin = len(mat2)                
mat2col = len(mat2[0])

print('matrix 1')       
print(mat1)      

print('matrix 2')       
print(mat1) 

matRes = [[] for y in range(mat1lin)]

print('matRes ',matRes)

def multiply_treads(id):
    
    def getLinha(matriz, n):
        return [i for i in matriz[n]]  # ou simplesmente return matriz[n]

    def getColuna(matriz, n):
        return [i[n] for i in matriz]

    start = int(id       * (mat1lin/thread_size))
    end   = int((id + 1 ) * (mat1lin/thread_size))
    print('thread ',id,' start ',start,' end ',end)
    for i in range(start,end):
        
        for j in range(mat2col):
            #print('thread ',id,' i ',i,' j ',j)
            # multiplica cada linha de mat1 por cada coluna de mat2;
            listMult = [x*y for x, y in zip(getLinha(mat1, i), getColuna(mat2, j))]
            #print('thread ',id,' listMult ',listMult)
            # e em seguida adiciona a matRes a soma das multiplicações
            matRes[i].append(sum(listMult))

thread_list = list()

for i in range(thread_size):
    t = threading.Thread(target=multiply_treads, args=(i,))
    thread_list.append(t)
    t.start()
    
for t in thread_list:
  t.join()
  
print('threads multiplcation result ')
pprint(matRes)
print('Numpy check ')
print(np.matmul(mat1, mat2))