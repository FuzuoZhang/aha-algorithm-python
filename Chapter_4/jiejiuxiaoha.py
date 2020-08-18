import numpy as np

minstep = 9999


def dfs(i,j,step,targetx,targety):
    global minstep
    global n
    global m
    if i==targetx and j==targety:
        if minstep>step:
            minstep=step
        return 
    fangxiang = [[0,1],[0,-1],[1,0],[-1,0]]
    for t in range(4):
        x,y=i+fangxiang[t][0], j+fangxiang[t][1]
        if x<0 or x>=n or y<0 or y>=m:
            continue
        if maze[x][y]==0 and book[x][y]==0:
            book[x][y]=1
            dfs(x,y,step+1,targetx,targety)
            book[x][y]=0
        
    
if __name__=="__main__":
    global maze
    maze = [[0,0,1,0],
            [0,0,0,0],
            [0,0,1,0],
            [0,1,0,0],
            [0,0,0,1]]
    startx, starty=0,0
    targetx,targety=3,2
    global n
    global m
    global book
    n,m = len(maze),len(maze[0])
    book = np.zeros((n,m),dtype=int)
    dfs(startx,starty,0,targetx,targety)
    print("最短路径长度为：", minstep)