import numpy as np



def Dijkstra():
    #O(N^2)
    e = [
        [0,1,12,float('inf'),float('inf'),float('inf')],
        [float('inf'),0,9,3,float('inf'),float('inf')],
        [float('inf'),float('inf'),0,float('inf'),5,float('inf')],
        [float('inf'),float('inf'),4,0,13,15],
        [float('inf'),float('inf'),float('inf'),float('inf'),0,4],
        [float('inf'),float('inf'),float('inf'),float('inf'),float('inf'),0]
    ]
    n=len(e)
    dist = np.array(e[0])
    book=np.zeros((n,),dtype=int)
    book[0]=1

    for k in range(n-1):
        mindist=float('inf')
        t = -1
        for i in range(n):
            if book[i]==0 and dist[i]<mindist:
                mindist=dist[i]
                t=i
        book[t]=1
        
        for i in range(n):
            if dist[i]>dist[t]+e[t][i]:
                dist[i]=dist[t]+e[t][i]

    print(dist)


if __name__=="__main__":
    #邻接矩阵存储图
    print("邻接矩阵存储图，Dijstra算法求第一个点到其他点的最短距离")
    Dijkstra()

    #用邻接表存储图
    print("邻接表存储图，Dijstra算法求第一个点到其他点的最短距离")
    u=np.zeros((5,),dtype=int)
    v=np.zeros((5,),dtype=int)
    w=np.zeros((5,),dtype=int)
    first=np.ones((4,),dtype=int)*(-1)
    next_=np.zeros((5,),dtype=int)
    m=5
    print("请输入5条边，每条边的输入格式为: 起点 终点 权值")
    for i in range(m):
        u[i],v[i],w[i]=map(int,input().split(' '))
        next_[i]=first[u[i]]
        first[u[i]]=i
    '''
    共5行输入，表示五条边
    0 3 9
    3 2 8
    0 1 5
    1 3 6
    0 2 7
    '''
    book=np.zeros((4,),dtype=int)
    dist=np.ones((4,),dtype=int)*float('inf')
    dist[0]=0

    for i in range(4):
        mindist = float('inf')
        t=-1
        for j in range(4):
            if book[j]==0 and dist[j]<mindist:
                mindist=dist[j]
                t=j
            k=first[t]
            while k!=-1:
                if dist[v[k]]>dist[t]+w[k]:
                    dist[v[k]]=dist[t]+w[k]
                k=next_[k]
    print(dist)


    #这里邻接表表示有些复杂，其实用链表结构就可以了