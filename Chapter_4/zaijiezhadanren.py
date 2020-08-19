import numpy as np

maxsum = 0
px,py=-1,-1

def getnum(x,y):
    num=0
    #向上
    i=x-1
    while maze[i][y]!="#":
        if maze[i][y]=="G":
            num+=1
        i-=1
    #向下
    i=x+1
    while maze[i][y]!="#":
        if maze[i][y]=="G":
            num+=1
        i+=1
    #向左
    j=y-1
    while maze[x][j]!="#":
        if maze[x][j]=="G":
            num+=1
        j-=1
    #向右
    j=y+1
    while maze[x][j]!="#":
        if maze[x][j]=="G":
            num+=1
        j+=1

    return num


def dfs(x,y):
    num = getnum(x,y)
    global maxsum
    global px
    global py
    if num>maxsum:
        maxsum=num
        px,py=x,y
    
    fangxiang = [[0,1],[0,-1],[1,0],[-1,0]]
    for i in range(4):
        tx,ty = x+fangxiang[i][0],y+fangxiang[i][1]
        if tx<0 or tx>n-1 or ty<0 or ty>m-1:
            continue
        if book[tx][ty]==0 and maze[tx][ty]==".":
            book[tx][ty]=1
            dfs(tx,ty)
    return 


class Site(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

def bfs(startx,starty):
    global maxsum
    global px
    global py
    book = np.zeros((n,m),dtype=int)
    q = np.empty((100,),dtype=Site)
    head=0
    tail=0
    q[tail]=Site(startx,starty)
    tail+=1
    book[startx][starty]
    maxsum = getnum(startx,starty)
    px,py=startx,starty
    fangxiang = [[0,1],[0,-1],[1,0],[-1,0]]
    while head<tail:
        tmp = q[head]
        for i in range(4):
            tx,ty =tmp.x+fangxiang[i][0],tmp.y+fangxiang[i][1]
            if tx<0 or tx>n-1 or ty<0 or ty>m-1:
                continue
            if book[tx][ty]==0 and maze[tx][ty]==".":
                q[tail]=Site(tx,ty)
                tail+=1
                book[tx][ty]=1
                num = getnum(tx,ty)
                if num>maxsum:
                    maxsum=num
                    px,py=tx,ty
        head+=1
    return 

        

if __name__=="__main__":
    global maze
    global n
    global m
    global book
    maze = [
        "#############",
        "#GG.GGG#GGG.#",
        "###.#G#G#G#G#",
        "#.......#..G#",
        "#G#.###.#G#G#",
        "#GG.GGG.#.GG#",
        "#G#.#G#.#.#.#",
        "##G...G.....#",
        "#G#.#G###.#G#",
        "#...G#GGG.GG#",
        "#G#.#G#G#.#G#",
        "#GG.GGG#G.GG#",
        "#############"
        ]
    n,m = len(maze),len(maze[0])
    book = np.zeros((n,m),dtype=int)
    startx,starty=3,3
    book[3][3]=1
    dfs(3,3)
    print("深度优先搜索，放置在位置：(%d,%d)，最多可消灭敌%d个敌人" %(px,py,maxsum))
    bfs(3,3)
    print("宽度优先搜索，放置在位置：(%d,%d)，最多可消灭敌%d个敌人" %(px,py,maxsum))