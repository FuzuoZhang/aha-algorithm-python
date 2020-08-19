import numpy as np


class Site(object):
    def __init__(self,x,y,putway):
        self.x=x
        self.y=y
        self.putway=putway


def dfs(x,y,front):
    global flag
    global top
    global stack
    global book
    global flag
    if x==n-1 and y==m:
        if front==1:
            flag=1
            t=0
            while t<=top:
                print("(%d,%d,%d)  " %(stack[t].x,stack[t].y,stack[t].putway), end="")
                t+=1
        return
    if x<0 or x>n-1 or y<0 or y>m-1:
        return 
    
    if book[x][y]==1:
        return
    book[x][y]=1
    #如果为直管
    if tubes[x][y]==5 or tubes[x][y]==6:
        if front==1:
            top+=1
            stack[top]=Site(x,y,5)
            dfs(x,y+1,1)
            top-=1
        if front==2:
            top+=1
            stack[top]=Site(x,y,5)
            dfs(x,y-1,2)
            top-=1
        if front==3:
            top+=1
            stack[top]=Site(x,y,6)
            dfs(x+1,y,3)
            top-=1
        if front==4:
            top+=1
            stack[top]=Site(x,y,6)
            dfs(x-1,y,4)
            top-=1
    
    #如果为弯管
    if tubes[x][y]>=1 and tubes[x][y]<=4:
        if front==1:
            top+=1
            stack[top]=Site(x,y,3)
            dfs(x+1,y,3)
            top-=1
            top+=1
            stack[top]=Site(x,y,4)
            dfs(x-1,y,4)
            top-=1
        if front==2:
            top+=1
            stack[top]=Site(x,y,1)
            dfs(x-1,y,4)
            top-=1
            top+=1
            stack[top]=Site(x,y,2)
            dfs(x+1,y,3)
            top-=1
        if front==3:
            top+=1
            stack[top]=Site(x,y,1)
            dfs(x,y+1,1)
            top-=1
            top+=1
            stack[top]=Site(x,y,4)
            dfs(x,y-1,2)
            top-=1
        if front==4:
            top+=1
            stack[top]=Site(x,y,2)
            dfs(x,y+1,1)
            top-=1
            top+1
            stack[top]=Site(x,y,3)
            dfs(x,y-1,2)
            top-=1
    book[x][y]=0

    return 


    

if __name__=="__main__":
    global tubes
    global n
    global m
    global book
    global stack
    global top
    global flag
    tubes = [
        [5,3,5,3],
        [1,5,3,0],
        [2,3,5,1],
        [6,1,1,5],
        [1,5,5,4]
    ]
    n,m=len(tubes),len(tubes[0])

    flag=0
    stack = np.empty((100,),dtype=Site)
    top=-1
    book = np.zeros((n,m),dtype=int)

    dfs(0,0,1)
    print()
    if flag==1:
        print("找到了联通方案")
    else:
        print("未找到联通方案")

