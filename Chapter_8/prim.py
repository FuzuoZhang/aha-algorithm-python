import numpy as np

def prim(e):
    #最简单的prim算法
    #时间复杂度：O(N^2)
    n=len(e)
    dist=np.zeros((n,),dtype=float)
    for i in range(n):
        dist[i]=e[0][i]
    book=np.zeros((n,),dtype=int)
    book[0]=1

    total_dist=0
    for i in range(n-1):
        mindist=float('inf')
        t=-1
        for j in range(n):
            if book[j]==0 and dist[j]<mindist:
                mindist=dist[j]
                t=j
        book[t]=1
        total_dist+=dist[t]
        for j in range(n):
            if book[j]==0 and e[t][j]<dist[j]:
                dist[j]=e[t][j]
    print("最小生成树的总权重：%d" %total_dist)


def siftdown(i,n,h,pos,dist):
    while i<=n//2-1:
        if dist[h[2*i+1]]<dist[h[i]]:
            t=2*i+1
        else:
            t=i
        if 2*i+2<=n-1:
            if dist[h[2*i+2]]<dist[h[t]]:
                t=2*i+2
        if t!=i:
            pos[h[i]]=t
            pos[h[t]]=i
            h[i],h[t]=h[t],h[i]
            i=t
        else:
            break

def siftup(i,h,pos,dist):
    while i>0:
        if dist[h[i]]<dist[h[(i-1)//2]]:
            t=(i-1)//2
            pos[h[i]]=t
            pos[h[t]]=i
            h[i],h[t]=h[t],h[i]
            i=t
        else:
            break


def pop(h,n,pos,dist):
    pos[h[0]]=-1 #表示该点已经不在堆中
    h[0]=h[n-1]
    pos[h[n-1]]=0
    siftdown(0,n-1,h,pos,dist)

def prim_opt(n,edges):
    #利用堆优化和邻接表对Prim进行优化
    m=len(edges)
    u=np.zeros((2*m,),dtype=int)
    v=np.zeros((2*m,),dtype=int)
    w=np.zeros((2*m,),dtype=int)
    for i in range(m):
        u[i]=edges[i][0]
        v[i]=edges[i][1]
        w[i]=edges[i][2]
        u[2*m-1-i]=edges[i][1]
        v[2*m-1-i]=edges[i][0]
        w[2*m-1-i]=edges[i][2]
    
    first=-1*np.ones((n,),dtype=int)
    next_=np.zeros((2*m,),dtype=int)
    for i in range(2*m):
        next_[i]=first[u[i]]
        first[u[i]]=i
    
    dist=float('inf')*np.ones((n,),dtype=float)
    dist[0]=0
    k=0 
    while k!=-1:
        ind = first[k]
        dist[v[ind]]=w[ind]
        k=next_[k]
    h=np.arange(n)
    pos=np.arange(n)
    
    #建堆：小顶堆
    for i in range(n//2-1,-1,-1):
        siftdown(i,n,h,pos,dist)

    #Prim核心算法
    total_dist=0
    for i in range(n):
        #取堆顶的点
        total_dist+=dist[h[0]]
        t=h[0]
        pop(h,n-i,pos,dist)
        k=first[t]
        while k!=-1:
            if dist[v[k]]>w[k]:
                dist[v[k]]=w[k]
                siftup(pos[v[k]],h,pos,dist)
            k=next_[k]
    
    print("最小生成树的总权重：%d" %total_dist)


if __name__=="__main__":
    n=6
    e = np.ones((n,n),dtype=int)*float('inf')
    for i in range(n):
        e[i][i]=0
    edges=[[0,1,1],[0,2,2],[1,2,6],[1,3,11],[2,3,9],[2,4,13],[3,4,7],[3,5,3],[4,5,4]]
    m=len(edges)
    for i in range(m):
        e[edges[i][0]][edges[i][1]]=edges[i][2]
        e[edges[i][1]][edges[i][0]]=edges[i][2]
    prim(e)
    prim_opt(n,edges)
    