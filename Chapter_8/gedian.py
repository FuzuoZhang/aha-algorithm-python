import numpy as np

index=0

def dfs(cur, father):
    global index
    global num
    global low
    global flag

    child=0
    #child记录在生成树中当前顶点cur的儿子个数

    index+=1
    num[cur]=index #当前顶点cur的时间戳
    low[cur]=index #当前顶点cur能够访问到最早顶点的时间戳，刚开始是自己
    for i in range(n): #枚举与当前顶点cur有边相连的顶点i
        if e[cur][i]==1:
            if num[i]==0: #顶点i的时间戳为0，说明顶点i没有被访问过
                child+=1
                dfs(i,cur)
                #更新当前顶点cur能访问到最早顶点的时间戳
                low[cur]=min(low[cur],low[i])
                #如果当前顶点不是根节点且满足low[i]>=num[cur]，则当前顶点为割点
                if cur!=root and low[i]>=num[cur]:
                    flag[cur]=1
                #如果当前顶点是根节点，在生成树中根节点必须要有两个儿子，则这个根节点才是割点
                if cur==root and child==2:
                    flag[cur]=1
            elif i!=father:
                #如果顶点i曾被访问过，且这个顶点不是当前顶点cur的父亲，说明
                #此时的i为cur的祖先，因此更新当前节点cur能访问到最早顶点的时间戳
                low[cur]=min(low[cur],num[i])
    return 


if __name__=="__main__":
    global n
    global e
    global root
    global num
    global low
    global flag

    n=6
    e=np.zeros((n,n),dtype=int)
    edges=[[0,3],[0,2],[3,1],[2,1],[1,4],[1,5],[4,5]]
    m=len(edges)
    for i in range(m):
        e[edges[i][0],edges[i][1]]=1
        e[edges[i][1],edges[i][0]]=1
        
    num=np.zeros((n,),dtype=int)
    low=np.zeros((n,),dtype=int)
    flag=np.zeros((n,),dtype=int)

    root=0
    dfs(0,0)
    for i in range(n):
        if flag[i]==1:
            print("顶点%d是割点" %i)