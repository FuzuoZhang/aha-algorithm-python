import numpy as np


class Site(object):
    def __init__(self,x,y,step):
        self.x = x
        self.y = y
        self.step = step


def bfs(maze, startx,starty,targetx,targety):
    n,m = len(maze),len(maze[0])
    book = np.zeros((n,m),dtype=int)
    q = np.empty((100,), dtype=Site)
    minstep = -1
    head = 0
    tail = 0
    q[0] = Site(startx,starty,0)
    book[startx,starty]=1
    tail+=1
    fangxiang = [[0,1],[0,-1],[1,0],[-1,0]]
    if startx==targetx and starty==targety:
        minstep=0
        return minstep
    while head<tail:
        tmp = q[head]
        for i in range(4):
            x,y = tmp.x+fangxiang[i][0], tmp.y+fangxiang[i][1]
            if x<0 or x>n-1 or y<0 or y>m-1:
                continue
            if x==targetx and y==targety:
                minstep=tmp.step+1
                return minstep
            if book[x][y]==0 and maze[x][y]==0:
                q[tail]=Site(x,y,tmp.step+1)
                book[x][y]=1
                tail+=1
        head+=1
    
    return -1


if __name__=="__main__":
    maze = [[0,0,1,0],
            [0,0,0,0],
            [0,0,1,0],
            [0,1,0,0],
            [0,0,0,1]]
    startx, starty=0,0
    targetx,targety=3,2
    minstep = bfs(maze, startx,starty,targetx,targety)
    if minstep<0:
        print("无可达路径")
    else:
        print("最短路径长度为：", minstep)