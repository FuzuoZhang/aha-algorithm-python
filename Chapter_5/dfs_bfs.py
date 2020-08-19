import numpy as np



def dfs(t,e,n):
    global top
    global stack
    global book
    if top==n-1:
        return 
    for i in range(n):
        if book[i]==0 and e[t][i]==1:
            book[i]=1
            top+=1
            stack[top]=i
            dfs(i,e,n)
    return 

def bianli_dfs(e,start):
    global stack
    global top
    global book
    n=len(e)
    book = np.zeros((n,),dtype=int)
    stack = np.zeros((n,),dtype=int)
    top=0
    stack[top]=start
    book[start]=1

    dfs(start,e,n)
    print("深度优先遍历结果")
    for i in range(0,top+1):
        print("%d " %stack[i], "")



def bianli_bfs(e,start):
    n = len(e)
    book = np.zeros((n,),dtype=int)
    q=np.zeros((n,),dtype=int)
    head=0
    tail=0

    stack=np.zeros((n,),dtype=int)
    top=-1
    q[tail]=start
    book[start]=1
    tail+=1
    top+=1
    stack[top]=start

    num=1
    flag=0
    while head<tail:
        tmp = q[head]
        for i in range(n):
            if e[tmp][i]==1 and book[i]==0:
                q[tail]=i
                tail+=1
                book[i]=1
                top+=1
                stack[top]=i
                num+=1
            if num>=n:
                flag=1
                break
        if flag==1:
            break
        head+=1

    print("广度优先遍历结果")
    for i in range(0,top+1):
        print("%d " %stack[i], "")


if __name__=="__main__":
    e = [
        [0,1,1,9999,1],
        [1,0,9999,1,9999],
        [1,9999,0,9999,1],
        [9999,1,9999,0,9999],
        [1,9999,1,9999,0]
    ]

    bianli_bfs(e,0)
    bianli_dfs(e,0)
