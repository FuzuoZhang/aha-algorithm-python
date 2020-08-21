import numpy as np


if __name__=="__main__":
    n,m=5,7
    u=np.zeros((m,),dtype=int)
    v=np.zeros((m,),dtype=int)
    w=np.zeros((m,),dtype=int)
    first=-1*np.ones((n,),dtype=int)
    next_=np.zeros((m,),dtype=int)
    
    print("请输入%d条边，每条边的输入格式为: 起点 终点 权值" %m)
    for i in range(m):
        u[i],v[i],w[i]=map(int,input().split(" "))
        next_[i]=first[u[i]]
        first[u[i]]=i
    
    dist=float('inf')*np.ones((n,),dtype=int)
    book=np.zeros((n,),dtype=int)
    dist[0]=0
    queue = np.zeros((100,),dtype=int)
    head=0
    tail=0
    queue[tail]=0
    tail+=1
    book[0]=1

    while head<tail:
        cur = queue[head]
        head+=1
        book[cur]=0
        k=first[cur]
        while k!=-1:
            if dist[v[k]]>dist[u[k]]+w[k]:
                dist[v[k]]=dist[u[k]]+w[k]
                if book[v[k]]==0:
                    queue[tail]=v[k]
                    tail+=1
                    book[v[k]]=1
            k=next_[k]
    
    #如果一个点进入队列超过n次，说明图中有负环路
    print("第一个点到其他各点的最短距离为：")
    print(dist)
        

