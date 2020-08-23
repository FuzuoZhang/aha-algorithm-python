import numpy as np

class Edge(object):
    def __init__(self,u,v,w):
        self.u=u
        self.v=v
        self.w=w
    

def quicksort(edges,left,right):
    if left>=right:
        return 
    tmp = edges[left].w
    j=right
    i=left
    while i<j:
        while i<j and edges[j].w>=tmp:
            j-=1
        while i<j and edges[i].w<=tmp:
            i+=1
        if i<j:
            edges[i],edges[j]=edges[j],edges[i]
    mid=i
    edges[i],edges[left]=edges[left],edges[i]
    quicksort(edges,left,mid-1)
    quicksort(edges,mid+1,right)
    

def getf(f,i):
    if f[i]==i:
        return i
    else:
        f[i]=getf(f,f[i])
        return f[i]
  
def merge(f,x,y):
    s=getf(f,x)
    t=getf(f,y)
    if s!=t:
        f[t]=s #注意！这里是更新y的祖先的祖先
        return 1
    else:
        return 0


if __name__=="__main__":
    edges=np.empty((9,),dtype=Edge)
    edges[0]=Edge(1,3,11)
    edges[1]=Edge(2,4,13)
    edges[2]=Edge(3,5,3)
    edges[3]=Edge(4,5,4)
    edges[4]=Edge(1,2,6)
    edges[5]=Edge(3,4,7)
    edges[6]=Edge(0,1,1)
    edges[7]=Edge(2,3,9)
    edges[8]=Edge(0,2,2)

    quicksort(edges,0,8)

    count=0
    total_dist=0
    f=np.arange(6)
    for i in range(9):
        if merge(f,edges[i].u,edges[i].v):
            total_dist+=edges[i].w
            count+=1
            print("加入边：%d-%d，权重为%d" %(edges[i].u,edges[i].v,edges[i].w))
        if count==5:
            break
    print("最小生成树的总权重为：%d" %total_dist)