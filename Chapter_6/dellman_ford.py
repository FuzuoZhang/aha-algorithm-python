import numpy as np


if __name__=="__main__":
    #顶点个数、边数
    n,m=5,5
     #用邻接表存储图
    print("邻接表存储图，Dellman-Ford算法求第一个点到其他点的最短距离")
    u=np.zeros((m,),dtype=int)
    v=np.zeros((m,),dtype=int)
    w=np.zeros((m,),dtype=int)
    print("请输入%d条边，每条边的输入格式为: 起点 终点 权值" %m)
    '''
    1 2 2
    0 1 -3
    0 4 5
    3 4 2
    2 3 3
    '''
    for i in range(m):
        u[i],v[i],w[i]=map(int,input().split(' '))

    dist=np.ones((n),dtype=int)*float('inf')
    dist[0]=0

    for k in range(n-1):
        check=0
        for i in range(m):
            if dist[v[i]]>dist[u[i]]+w[i]:
                dist[v[i]]=dist[u[i]]+w[i]
                check=1
        if check==0:
            break
    
    flag=0
    for i in range(m):
        if dist[v[i]]>dist[u[i]]+w[i]:
            flag=1
    if flag==1:
        print("存在负环路")
    else:
        print("第一个点到其他各点的最短距离为：")
        print(dist)

