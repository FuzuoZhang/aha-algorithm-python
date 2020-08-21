import numpy as np





if __name__=="__main__":
    e = [
        [0,2,6,4],
        [float('inf'),0,3,float('inf')],
        [7,float('inf'),0,1],
        [5,float('inf'),12,0]
    ]
    n = len(e)

    #Floyd核心算法
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if e[i][j]>e[i][k]+e[k][j]:
                    e[i][j]=e[i][k]+e[k][j]
    
    for i in range(n):
        for j in range(n):
            print("%2d " %e[i][j], end="")
        print()