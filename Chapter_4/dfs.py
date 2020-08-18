import numpy as np 

total = 0

def quanpailie(n):
    global a
    global book
    global total 
    total = 0
    #搜索1-n的所有全排列
    a = np.zeros((n+1,), dtype=int)
    book = np.zeros((n+1,), dtype=int)
    dfs1(1)


def dfs1(step):
    #全排列的dfs
    global total
    if step==n+1:
        total = total+1
        print(a[1:])
        return 
    for i in range(1,n+1):
        if book[i]==0:
            a[step]=i
            book[i]=1
            dfs1(step+1)
            book[i]=0
        else:
            continue
    return 

def dfs2(step):
    global total
    if step==n+1:
        if a[1]*100+a[2]*10+a[3]+a[4]*100+a[5]*10+a[6]==a[7]*100+a[8]*10+a[9]:
            print("%d%d%d+%d%d%d=%d%d%d" %(a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9]))
            total+=1
        return 
    for i in range(1,10):
        if book[i]==0:
            a[step]=i
            book[i]=1
            dfs2(step+1)
            book[i]=0
    return 
        
def fun():
    #???+???=???
    #要求将数字1-9填入以上各?处，使等式成立，且每个数字只能使用一次
    global n
    global total
    global a
    global book
    n=9
    total = 0
    a = np.zeros((n+1,),dtype=int)
    book = np.zeros((n+1),dtype=int)
    dfs2(1)
    print("可能的解的个数为：%d" %((total+1)//2))

if __name__=="__main__":
    global n
    n = 4
    quanpailie(n)
    print("可能的全排列个数为：%d" %total)
    fun()