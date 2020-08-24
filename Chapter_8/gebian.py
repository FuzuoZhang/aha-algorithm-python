import numpy as np

index=0

def dfs(cur, father):
    global index
    global num
    global low


    index+=1
    num[cur]=index 
    low[cur]=index 
    for i in range(n): #枚举与当前顶点cur有边相连的顶点i
        if e[cur][i]==1:
            if num[i]==0: #顶点i的时间戳为0，说明顶点i没有被访问过
                dfs(i,cur)
                #更新当前顶点cur能访问到最早顶点的时间戳
                low[cur]=min(low[cur],low[i])
                if low[i]>num[cur]:
                    print("割边：%d--%d" %(cur,i))
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

    n=6
    e=np.zeros((n,n),dtype=int)
    edges=[[0,3],[0,2],[3,1],[2,1],[1,4],[4,5]]
    m=len(edges)
    for i in range(m):
        e[edges[i][0],edges[i][1]]=1
        e[edges[i][1],edges[i][0]]=1
        
    num=np.zeros((n,),dtype=int)
    low=np.zeros((n,),dtype=int)


    root=0
    dfs(0,0)
    