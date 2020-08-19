import numpy as np

class City(object):
    def __init__(self,t,time):
        self.t=t
        self.time=time


if __name__=="__main__":
    e = [
        [0,1,1,0,0],
        [1,0,1,1,0],
        [1,1,0,1,1],
        [0,1,1,0,1],
        [0,0,1,1,0]
    ]
    n = len(e)
    q = np.empty((n,),dtype=City)
    book = np.zeros((n,),dtype=int)
    head=0
    tail=0
    q[tail]=City(0,0)
    tail+=1
    book[0]=1
    flag=0

    while head<tail:
        tmp = q[head]
        head+=1
        for i in range(n):
            if book[i]==0 and e[tmp.t][i]==1:
                if i==4:
                    flag=1
                    trans_time = tmp.time+1
                    break
                else:
                    book[i]=1
                    q[tail]=City(i,tmp.time+1)
                    tail+=1
        if flag==1:
            break
    
    print("最少转机次数：%d" %trans_time)