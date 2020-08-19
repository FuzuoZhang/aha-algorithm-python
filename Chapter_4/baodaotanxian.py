import numpy as np

class Site(object):
    def __init__(self,x,y):
        self.x =x
        self.y = y
    
#广度优先搜索，计算（startx,starty）所在小岛的面积
def getarea_bfs(sites,startx,starty):
    n,m = len(sites),len(sites[0])
    book = np.zeros((n,m),dtype=int)

    area = 0
    q = np.empty((100,),dtype=Site)
    head,tail=0,0
    q[tail]=Site(startx,starty)
    tail+=1
    book[startx][starty]=1
    area+=1
    
    fangxiang = [[0,1],[0,-1],[1,0],[-1,0]]
    #广度优先搜索
    while head<tail:
        tmp = q[head]
        for i in range(4):
            tx,ty = tmp.x+fangxiang[i][0], tmp.y+fangxiang[i][1]
            if tx<0 or tx>n-1 or ty<0 or ty>m-1:
                continue
            if book[tx][ty]==0 and sites[tx][ty]>0:
                area+=1
                q[tail]=Site(tx,ty)
                tail+=1
                book[tx][ty]=1
        head+=1
    return area

#深度优先搜索，计算（startx,starty）所在小岛的面积
def getarea_dfs(sites,startx,starty):
    #用栈结构实现dfs（递归就是利用栈的思想）
    n,m=len(sites),len(sites[0])
    stack = np.empty((100,),dtype=Site)
    book = np.zeros((n,m),dtype=int)
    top=-1
    
    top+=1
    stack[top]=Site(startx,starty)
    book[startx][starty]=1
    area = 1
    
    fangxiang = [[0,1],[0,-1],[1,0],[-1,0]]
    while top>=0:
        tmp = stack[top]
        top-=1
        for i in range(4):
            tx,ty = tmp.x+fangxiang[i][0],tmp.y+fangxiang[i][1]
            if tx<0 or tx>n-1 or ty<0 or tx>m-1:
                continue
            if book[tx][ty]==0 and sites[tx][ty]>0:
                area+=1
                top+=1
                stack[top]=Site(tx,ty)
                book[tx][ty]=1
    return area

#深度优先搜索，计算地图上独立岛屿的个数
def getnum_dfs(sites):
    n,m = len(sites),len(sites[0])
    stack=np.empty((100,),dtype=Site)
    sites_copy = sites.copy()
    num=0
    fangxiang = [[0,1],[0,-1],[1,0],[-1,0]]
    mark=0
    for i in range(n):
        for j in range(m):
            top=-1
            if sites_copy[i][j]>0:
                num+=1
                top+=1
                stack[top]=Site(i,j)
                mark-=1
                sites_copy[i][j]=mark
                while top>=0:
                    tmp = stack[top]
                    top-=1
                    for t in range(4):
                        tx,ty=tmp.x+fangxiang[t][0],tmp.y+fangxiang[t][1]
                        if tx<0 or tx>n-1 or ty<0 or ty>m-1:
                            continue
                        if sites_copy[tx][ty]>0:
                            top+=1
                            stack[top]=Site(tx,ty)
                            sites_copy[tx][ty]=mark
    return sites_copy, num



if __name__=="__main__":
    sites = [
        [1,2,1,0,0,0,0,0,2,3],
        [3,0,2,0,1,2,1,0,1,2],
        [4,0,1,0,1,2,3,2,0,1],
        [3,2,0,0,0,1,2,4,0,0],
        [0,0,0,0,0,0,1,5,3,0],
        [0,1,2,1,0,1,5,4,3,0],
        [0,1,2,3,1,3,6,2,1,0],
        [0,0,3,4,8,9,7,5,0,0],
        [0,0,0,3,7,8,6,0,1,2],
        [0,0,0,0,0,0,0,0,1,0]
    ]
    startx,starty=5,7
    area = getarea_bfs(sites,startx,starty)
    print("广度优先搜索：岛屿的面积为%d" %area)
    area = getarea_dfs(sites,startx,starty)
    print("深度优先搜索：岛屿的面积为%d" %area)

    #计算独立岛屿个数
    islands, num = getnum_dfs(sites)
    print("深度优先搜索：独立岛屿的个数为%d" %num)
    print("岛屿的分布为：")
    for i in range(len(islands)):
        for j in range(len(islands[0])):
            print("%3d" %islands[i][j], end="")
        print()