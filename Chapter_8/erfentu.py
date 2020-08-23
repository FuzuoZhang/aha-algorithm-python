import numpy as np


def dfs_1(i,n,e,match,matchnum):
    #对于每一个女生i，搜索每一个可能的j都与其进行匹配
    global largest_match
    global best_match
    if i==n:
        if matchnum>largest_match:
            largest_match=matchnum
            best_match=match.copy()
        return 
    for j in range(n):
        flag=0
        if match[j]==-1: 
            if e[i][j]==1:
                matchnum+=1
                flag=1
            match[j]=i
            dfs_1(i+1,n,e,match,matchnum)
            match[j]=-1
        if flag==1:
            matchnum-=1
    return 

def find_max_erfentu(e):
    #搜索所有的匹配方案寻找匹配数最大的一种
    n=len(e)
    match=-1*np.ones((n,),dtype=int)
    global largest_match
    global best_match
    largest_match=0
    best_match=None
    dfs_1(0,n,e,match,0)
    print("最大配对数为：",largest_match)
    print("配对方案为：")
    for j in range(n):
        if best_match[j]>-1:
            print("女生%d--男生%d" %(best_match[j],j))


def dfs(u,n,book,e,match):
    for i in range(n):
        if book[i]==0 and e[u][i]==1:
            book[i]=1
            if match[i]==-1 or dfs(match[i],n,book,e,match):
                match[i]=u
                return 1
    return 0



def find_maxerfentu_opt(e):
    #寻找增广路策略：搜索所有的匹配方案寻找匹配数最大的一种
    n=len(e)
    match=-1*np.ones((n,),dtype=int)
    book=np.zeros((n,),dtype=int)
    matchnum=0
    for i in range(n):
        book=np.zeros((n,),dtype=int)
        if(dfs(i,n,book,e,match)):
            matchnum+=1
    print("最大匹配数为：%d" %matchnum)
        
if __name__=="__main__":
    n=3
    e=np.zeros((n,n),dtype=int)
    e[0][0]=1
    e[0][1]=1
    e[1][1]=1
    e[1][2]=1
    e[2][0]=1

    print("搜索所有匹配方案，寻找匹配数最大的一种")
    find_max_erfentu(e)
    print()
    print("寻找增广路策略，寻找最大匹配数")
    find_maxerfentu_opt(e)
