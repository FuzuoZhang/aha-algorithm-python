import numpy as np

mindist=9999

def dfs(s,t,dist):
    global mindist
    if dist>=mindist:
        return 
    if s==t:
        if dist<mindist:
            mindist=dist
        return
    for i in range(n):
        if book[i]==0 and e[s][i]>0:
            book[i]=1
            dfs(i,t,dist+e[s][i])
            book[i]=0
    return 
if __name__=="__main__":
    global e
    global book
    global n 

    '''
    e = [
        [0,2,4,-1,10],
        [2,0,3,-1,7],
        [4,3,0,4,3],
        [-1,-1,4,0,5],
        [10,7,3,5,0]
    ]
    '''
    e = [
        [0,2,-1,-1,10],
        [-1,0,3,-1,7],
        [4,-1,0,4,-1],
        [-1,-1,-1,0,5],
        [-1,-1,3,-1,0]
    ]
    n=len(e)
    book = np.zeros((n,),dtype=int)
    book[0]=1
    dfs(0,4,0)
    print("最短路径长度为：%d" %mindist)