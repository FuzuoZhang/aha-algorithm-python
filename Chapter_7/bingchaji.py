import numpy as np

def getf(f,i):
    if f[i]==i:
        return i
    else:
        f[i]=getf(f,f[i])
        return f[i]

def merge(f,x,y):
    s = getf(f,x)
    t = getf(f,y)
    if s!=t:
        f[t]=s
    return 

if __name__=="__main__":
    n=10
    f=np.arange(n)
    m=9
    #输入线索
    clues = [[1,2],[3,4],[5,2],[4,6],[2,6],[8,7],[9,7],[1,6],[2,4]]
    for i in range(m):
        x,y=clues[i][0],clues[i][1]
        merge(f,x,y)
    '''
    print("请输入%d条线索" %m)
    for i in range(m):
        x,y=map(int,input().split(" "))
        merge(f,x,y)
    '''
    print(f)
    total=0
    for i in range(n):
        if f[i]==i:
            total+=1
    print("总共有%d个独立组合。" %total)

    